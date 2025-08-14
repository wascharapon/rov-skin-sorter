<template>
  <div>
    <div>
      <b-modal
        id="class-skin-rov-table"
        size="xl"
        hide-footer
        body-class="bg-dark text-white"
        header-class="bg-dark text-white"
      >
        <template #modal-header>
          <div
            class="w-100 font-size-18 d-block d-flex align-items-center modern-modal-header"
          >
            <b-icon icon="trophy" class="mr-2" />
            <span class="modern-title">ข้อมูลระดับ</span>
          </div>
          <fa-icon
            icon="close"
            class="me-1 cursor-pointer modern-close-btn"
            @click="$bvModal.hide($attrs.id)"
          />
        </template>
        <div class="d-flex d-block flex-wrap">
          <div
            v-for="(item, index) in classSkinRov"
            :key="index"
            class="badge text-white mr-2 mb-2 px-3"
            :style="{ backgroundColor: item.color }"
          >
            <h5 class="mb-1">
              {{ index + 1 }} - {{ item.name }}
            </h5>
          </div>
        </div>
      </b-modal>
    </div>
    <div class="modern-bg py-2" style="min-height: 100vh">
      <div class="container-fluid py-3 text-white modern-container">
        <div id="table-skin-header">
          <div
            class="compact-header-section d-flex flex-wrap"
            :class="{ 'mb-3': isHeaderVisible }"
          >
            <b-button
              class="compact-toggle-btn modern-compact-btn mb-2 mr-2"
              variant="outline-light"
              size="sm"
              @click="toggleHeaderVisibility"
            >
              <b-icon
                :icon="isHeaderVisible ? 'chevron-up' : 'chevron-down'"
                class="mr-1"
              />
              {{ isHeaderVisible ? "แผงควบคุม" : "แสดงแผงควบคุม" }}
            </b-button>

            <b-button
              class="compact-reset-btn modern-compact-btn modern-btn-warning mb-2 mr-2"
              variant="warning"
              size="sm"
              :disabled="isSaving"
              @click="resetDataSkinTable"
            >
              <b-icon icon="arrow-clockwise" class="mr-1" />
              เริ่มต้นใหม่
            </b-button>

            <b-button
              class="compact-toggle-item modern-compact-btn mb-2 mr-2"
              :class="
                form.isEnableItem
                  ? 'modern-btn-success'
                  : 'modern-btn-secondary'
              "
              :variant="form.isEnableItem ? 'success' : 'outline-secondary'"
              size="sm"
              @click="form.isEnableItem = !form.isEnableItem"
            >
              <b-icon
                :icon="form.isEnableItem ? 'eye' : 'eye-slash'"
                class="mr-1"
              />
              {{ form.isEnableItem ? "ซ่อนตำแหน่ง" : "แสดงตำแหน่ง" }}
            </b-button>

            <b-button
              class="compact-facebook-btn modern-compact-btn modern-btn-facebook mb-2"
              size="sm"
              :disabled="isSaving"
              @click="
                goToBlankPage(
                  'https://www.facebook.com/share/18DD4E54Jg/?mibextid=wwXIfr'
                )
              "
            >
              <b-icon icon="facebook" class="mr-1" />
              ร้าน Moji G Moji รับทำปกไอดี Rov สนใจคลิก !!!!
            </b-button>
          </div>

          <!-- Collapsible Header Container -->
          <b-collapse
            id="content-table-skin-header"
            v-model="isHeaderVisible"
            class="ipad-header-container"
          >
            <!-- Grid Controls Section -->
            <div class="ipad-control-section mb-4">
              <div class="section-header">
                <b-icon icon="grid-3x3-gap" class="section-icon" />
                <h5 class="section-title">
                  ตั้งค่าตาราง
                </h5>
              </div>
              <div class="ipad-grid-controls">
                <div class="grid-input-group">
                  <b-form-group
                    label="แนวนอน (Row)"
                    class="modern-form-group ipad-form-group"
                  >
                    <b-form-input
                      v-model="formData.column"
                      type="number"
                      placeholder="3 - 12"
                      class="modern-input ipad-input"
                    />
                  </b-form-group>
                </div>
                <div class="grid-input-group">
                  <b-form-group
                    label="แนวตั้ง (Column)"
                    class="modern-form-group ipad-form-group"
                  >
                    <b-form-input
                      v-model="formData.row"
                      type="number"
                      placeholder="3 - 12"
                      class="modern-input ipad-input"
                    />
                  </b-form-group>
                </div>
                <div class="grid-input-group">
                  <b-form-group
                    label-align="center"
                    :label="`ความกว้าง (${formData.width}%)`"
                    class="modern-form-group ipad-form-group"
                  >
                    <b-form-input
                      v-model="formData.width"
                      type="range"
                      min="30"
                      max="100"
                      :step="1"
                      class="modern-range ipad-range"
                    />
                  </b-form-group>
                </div>
                <div class="grid-apply-btn">
                  <b-button
                    class="modern-btn modern-btn-primary ipad-primary-btn"
                    variant="primary"
                    @click="applyGridDimensions"
                  >
                    <b-icon icon="grid-3x3-gap" class="mr-2" />
                    ปรับใช้งาน
                  </b-button>
                </div>
              </div>
            </div>
            <!-- File Management Section -->
            <div class="ipad-control-section">
              <div class="section-header">
                <b-icon icon="folder" class="section-icon" />
                <h5 class="section-title">
                  การจัดการไฟล์
                </h5>
              </div>
              <div class="ipad-file-controls">
                <div class="file-input-wrapper">
                  <b-form-file
                    class="modern-file-input ipad-file-input"
                    accept=".json"
                    browse-text="เลือกไฟล์"
                    placeholder="เลือกไฟล์ข้อมูล JSON"
                    @change="importDataFromFile"
                  >
                    <template #file-name>
                      <b-icon icon="file-earmark-arrow-up" class="mr-2" />
                      นำเข้าข้อมูล
                    </template>
                  </b-form-file>
                </div>
                <div class="file-action-buttons">
                  <b-button
                    class="modern-btn modern-btn-primary ipad-file-btn"
                    variant="primary"
                    :disabled="isSaving"
                    @click="exportDataToFile"
                  >
                    <b-icon icon="file-earmark-arrow-down" class="mr-2" />
                    ส่งออกเป็น JSON
                  </b-button>
                  <b-button
                    class="modern-btn modern-btn-success ipad-file-btn"
                    variant="success"
                    :disabled="isSaving || !isCanSave"
                    @click="saveTableAsImage"
                  >
                    <b-icon icon="image" class="mr-2" />
                    บันทึกรูปภาพ
                  </b-button>
                </div>
              </div>
            </div>
          </b-collapse>
          <b-row id="select-skin-row" class="mt-3">
            <b-col cols="6">
              <b-row>
                <b-col id="display-select-skin-rov" lg="2" md="4" cols="12">
                  <b-img
                    :src="selectSkinRovOnTable.image || defaultSkinImage"
                    alt="Selected Skin Image"
                    class="img-fluid fit-col-image mt-2"
                  />
                </b-col>
                <b-col id="select-skin-rov" lg="10" md="8" cols="12">
                  <b-form-group
                    :label="`กำลังเลือก : ${selectSkinRovOnTable.key || 0} -  ${
                      !selectSkinRovOnTable?.name
                        ? 'ว่าง'
                        : selectSkinRovOnTable?.name
                    }`"
                    class="modern-form-group text-nowrap"
                  >
                    <Multiselect
                      ref="selectSkinRov"
                      v-model="selectSkinRov"
                      class="mt-2"
                      :options="rov"
                      placeholder="เลือกสกิน ROV"
                      label="name"
                      track-by="id"
                      :custom-label="customLabelSkin"
                      :close-on-select="false"
                      :clear-on-select="false"
                      tag-placeholder="กด Enter เพื่อเพิ่มสกินใหม่"
                      :options-limit="9"
                      :max-height="700"
                      :max="1"
                      :limit="1"
                    >
                      <template #option="{ option }">
                        <div class="option-with-image">
                          <img
                            :src="option.image"
                            alt="icon"
                            class="option-image"
                          >
                          <h1>
                            {{ option.name }}
                          </h1>
                          <h4 class="mx-2">
                            ({{ option.base }})
                          </h4>
                        </div>
                      </template>

                      <template #tag="{ option, remove }">
                        <div class="selected-tag">
                          <img
                            :src="option.image"
                            alt="icon"
                            class="tag-image"
                          >
                          <span>{{ option.name }}</span>
                          <button @click="remove(option)">
                            x
                          </button>
                        </div>
                      </template>

                      <template #noResult>
                        <div class="text-center py-2">
                          <p class="text-muted mb-0">
                            ไม่พบสกินตามที่ค้นหา
                          </p>
                        </div>
                      </template>
                    </Multiselect>
                  </b-form-group>
                </b-col>
              </b-row>
            </b-col>
            <b-col cols="3" class="d-flex align-items-center">
              <b-button
                class="w-100 mt-4 modern-btn modern-btn-warning"
                variant="warning"
                @click="sortDataFollowPosition"
              >
                <b-icon icon="sort-numeric-down" class="mr-2" />
                เรียง
              </b-button>
            </b-col>
            <b-col cols="3" class="d-flex align-items-center">
              <b-button
                class="w-100 mt-4 modern-btn modern-btn-success"
                variant="success"
                :disabled="isSaving || !isCanSave"
                @click="saveTableAsImage"
              >
                <b-icon icon="image" class="mr-2" />
                {{ isSaving ? "บันทึก..." : "บันทึก" }}
              </b-button>
            </b-col>
          </b-row>
        </div>
      </div>

      <div
        class="d-flex justify-content-center modern-container mt-2"
        style="min-height: 78vh"
      >
        <div
          :style="{
            width: widthTableSkinRov * form.column + 'px',
            background: 'transparent',
          }"
          class="skin-box"
        >
          <draggable
            id="table-skin"
            v-model="data"
            class="grid-wrapper"
            :style="`grid-template-columns: repeat(${form.column}, ${widthTableSkinRov}px);`"
            group="skins"
            :disabled="false"
            ghost-class="ghost"
            chosen-class="chosen"
            drag-class="drag"
            @start="onDragStart"
            @end="onDragEnd"
          >
            <div
              v-for="item in visibleData"
              :key="`skin-${item.key}`"
              class="skin-item cursor-pointer"
              :style="`width: ${widthTableSkinRov}px;`"
              @click="onSelectSkinRovOnTable(item)"
            >
              <div class="skin-wrapper">
                <img
                  :width="`${widthTableSkinRov}px`"
                  :src="item.image"
                  alt="skin image"
                  class="img-fluid"
                  :style="{ height: `${widthTableSkinRov * 1.5 - 17}px` }"
                >
                <div v-if="!isSaving" class="skin-future-remove text-white">
                  <b-icon
                    :style="{ width: '150%', height: '150%' }"
                    icon="x"
                    class="btn-close"
                    @click.stop="onRemoveSkinRov(item)"
                  />
                </div>
                <div
                  v-if="item.base && form.isEnableItem && !isSaving"
                  class="skin-future"
                >
                  <div class="d-flex justify-content-center align-items-center">
                    <span class="text-white" style="font-size: 150%">
                      <b-badge variant="primary">
                        {{ item.base }}
                      </b-badge>
                      <br>
                      <b-badge
                        :variant="item.position ? 'warning' : 'danger'"
                        class="ml-1"
                      >
                        {{ item.position ? item.position : "ไม่ระบุ" }}
                      </b-badge>
                    </span>
                  </div>
                </div>
                <div class="drag-handle">
                  <b-icon icon="grip-vertical" class="text-white" />
                </div>
              </div>
            </div>
          </draggable>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import html2canvas from 'html2canvas'
import { rov } from '~/lib/skin'
import { IRovSkin, IRovSkinOnTable } from '~/model/rov'
export default Vue.extend({
  data() {
    return {
      $cachedRov: null as IRovSkin[] | null,
      $cachedWidthCalc: 0,
      $lastFormState: '',
      $saveDebounceTimer: null as any,
      selectSkinRov: [] as IRovSkin[],
      selectSkinRovOnTable: {} as IRovSkinOnTable,
      selectSkinForSwap: {} as IRovSkinOnTable,
      isDragging: false,
      isSaving: false,
      keyLocalStorage: 'rov-skin-sorter',
      formData: {
        column: 15,
        row: 5,
        width: 100
      } as {
        column: number;
        row: number;
        width: number;
      },
      form: {
        column: 15,
        row: 5,
        width: 100, // Percentage of the container width
        isEnableItem: false
      } as {
        column: number;
        row: number;
        width: number;
        isEnableItem: boolean;
      },
      data: [] as IRovSkinOnTable[],
      isHeaderVisible: true,
      classSkinRov: [
        { name: 'Collaboration Limited', color: '#a62828' },
        { name: 'Bleach เทพมรณะ', color: '#1c1c1c' },
        { name: 'DEMON SLAYER', color: '#e65100' },
        { name: 'Jujutsu Kaisen', color: '#3e2723' },
        { name: 'Sword art Online', color: '#1a237e' },
        { name: 'Hunter X Hunter', color: '#2e7d32' },
        { name: 'Harley Quinn', color: '#880e4f' },
        { name: 'Witching Hour', color: '#4a148c' },
        { name: 'Mythical', color: '#b71c1c' },
        { name: 'Dimension Breaker', color: '#4527a0' },
        { name: 'Dragon Legacy (Red)', color: '#263238' },
        { name: 'RockStar.', color: '#1e88e5' },
        { name: 'ANNIV.', color: '#6a1b9a' },
        { name: 'SNK', color: '#01579b' },
        { name: 'SailorMoon', color: '#c2185b' },
        { name: 'Miracle', color: '#ef6c00' },
        { name: 'WAVE', color: '#1565c0' },
        { name: 'Dragon Legacy (yellow)', color: '#455a64' },
        { name: 'Serpent Saga', color: '#bf360c' },
        { name: 'EVO', color: '#00838f' },
        { name: 'ESTEEM', color: '#4a148c' },
        { name: 'Ultimate', color: '#263238' },
        { name: 'Miss Rov', color: '#b0003a' },
        { name: 'Magic School', color: '#311b92' },
        { name: '5v5FEST', color: '#ef6c18' },
        { name: 'Vip', color: '#5d4037' },
        { name: 'RPL', color: '#b71c1c' },
        { name: 'FMVP', color: '#4e342e' },
        { name: 'ANNIV.(veeres,forentino)', color: '#7b1fa2' },
        { name: 'Prestige', color: '#6d4c41' },
        { name: 'AIC 2018', color: '#8d6e63' },
        { name: 'สงกรานต์', color: '#00695c' },
        { name: 'Christmas', color: '#ad1457' },
        { name: 'New Year', color: '#1b5e20' },
        { name: 'Halloween', color: '#ff6f00' },
        { name: 'Snow Festival', color: '#006064' },
        { name: 'Valentine', color: '#c2185b' },
        { name: 'Legend', color: '#795548' },
        { name: 'VaLor', color: '#424242' },
        { name: 'SUPREME', color: '#9c27b0' },
        { name: 'Limited', color: '#512da8' }
      ]
    }
  },
  computed: {
    repoGitHubAssetsImagesSkin() {
      return 'https://github.com/wascharapon/rov-skin-sorter/blob/main/assets/images/skin/'
    },
    rov() {
      // Use getter method to handle caching without side effects
      return this.getCachedRovData()
    },
    visibleData() {
      // Pre-compute visible data to avoid slice operation in template
      return this.data.slice(0, this.form.row * this.form.column)
    },
    defaultSkinImage() {
      return 'https://github.com/wascharapon/rov-skin-sorter/blob/main/assets/images/skin/default.jpeg?raw=true'
    },
    defaultSkinItemImage() {
      return require('~/assets/images/item/default.png')
    },
    timeStamp() {
      const now = new Date()
      const yyyy = now.getFullYear()
      const mm = String(now.getMonth() + 1).padStart(2, '0')
      const dd = String(now.getDate()).padStart(2, '0')
      const hh = String(now.getHours()).padStart(2, '0')
      const mi = String(now.getMinutes()).padStart(2, '0')
      const ss = String(now.getSeconds()).padStart(2, '0')
      return `${yyyy}-${mm}-${dd}_${hh}-${mi}-${ss}`
    },
    fileNameSystem() {
      return 'rov-skin-table-draggable'
    },
    widthTableSkinRov() {
      if (!process.client || typeof window === 'undefined') {
        return this.form.width * 1.5
      }
      // Use getter method to handle caching without side effects
      return this.getCachedWidth()
    },
    isCanSave() {
      const dataLength = this.data.length
      return (
        (dataLength === this.form.row * this.form.column) &&
        this.data[0].id &&
        this.data[0].image &&
        this.data[dataLength - 1].id &&
        this.data[dataLength - 1].image
      )
    }
  },
  watch: {
    form: {
      handler() {
        // Clear width calculation cache when form changes
        this.$cachedWidthCalc = 0
        this.$lastFormState = ''
        this.setDataForTable()
        // Debounce localStorage saves to reduce frequent writes
        if (this.$saveDebounceTimer) {
          clearTimeout(this.$saveDebounceTimer)
        }
        this.$saveDebounceTimer = setTimeout(() => {
          this.saveDataToLocalStorage()
        }, 300)
      },
      deep: true
    },
    selectSkinRov(val: IRovSkin) {
      if (val) {
        this.selectSkinRovOnTable = {
          ...this.selectSkinRovOnTable,
          ...val
        } as IRovSkinOnTable
        const index = this.data.findIndex(
          item => item.key === this.selectSkinRovOnTable.key
        )
        if (index !== -1) {
          this.data[index].id = this.selectSkinRovOnTable.id
          this.data[index].name = val.name
          this.data[index].image = val.image
          this.data[index].base = val.base
          this.data[index].position = val.position
        }
        this.selectSkinRov = undefined
        if (this.selectSkinRovOnTable.key < this.form.row * this.form.column) {
          this.selectSkinRovOnTable = {
            ...this.selectSkinRovOnTable,
            ...this.data[this.selectSkinRovOnTable.key]
          } as IRovSkinOnTable
        }
        this.saveDataToLocalStorage()
      }
    },
    data: {
      handler() {
        this.data.forEach((item, index) => {
          item.key = index + 1
        })
      },
      deep: true
    }
  },
  created() {
    this.setDataForTable()
    if (process.client && typeof window !== 'undefined') {
      const stored = localStorage.getItem('rov-header-visible')
      if (stored !== null) {
        this.isHeaderVisible = stored === 'true'
      }
    }
    setTimeout(() => {
      this.loadDataFromLocalStorage()
    }, 1000)
  },
  mounted() {
    window.addEventListener('keydown', this.handleKeyDown)
  },
  beforeDestroy() {
    window.removeEventListener('keydown', this.handleKeyDown)
    // Clean up timers
    if (this.$saveDebounceTimer) {
      clearTimeout(this.$saveDebounceTimer)
    }
  },
  methods: {
    getCachedRovData() {
      if (!this.$cachedRov) {
        this.$cachedRov = Object.freeze(
          rov.map((item) => {
            return {
              ...item,
              image:
                `${this.repoGitHubAssetsImagesSkin}${item.image}?raw=true` ||
                this.defaultSkinItemImage
            } as IRovSkin
          })
        )
      }
      return this.$cachedRov as IRovSkin[]
    },
    getCachedWidth() {
      const currentFormState = `${this.form.column}-${this.form.width}`
      if (!this.$cachedWidthCalc || this.$lastFormState !== currentFormState) {
        const containerElement = document.querySelector('.modern-container')
        let availableWidth = window.innerWidth * 0.9 // Fallback
        if (containerElement) {
          const containerStyle = window.getComputedStyle(containerElement)
          const containerWidth = containerElement.clientWidth
          const paddingLeft = parseFloat(containerStyle.paddingLeft) || 0
          const paddingRight = parseFloat(containerStyle.paddingRight) || 0
          availableWidth = containerWidth - paddingLeft - paddingRight
        }
        // Calculate maximum width per skin item
        const maxWidthPerItem =
          Math.floor(availableWidth / this.form.column) - 3.33 // 5px margin
        // Calculate desired width based on form percentage
        const desiredWidth =
          (this.form.width * availableWidth) / 100 / this.form.column
        // Cache the result
        this.$cachedWidthCalc = Math.min(maxWidthPerItem, desiredWidth)
        this.$lastFormState = currentFormState
      }
      return this.$cachedWidthCalc
    },
    goToBlankPage(url: string) {
      window.open(url, '_blank')
    },
    handleKeyDown(event: KeyboardEvent) {
      if (event.key.toLowerCase() === 'e' && event.metaKey) {
        event.preventDefault()
        const multiselect = this.$refs.selectSkinRov as any
        if (multiselect) {
          multiselect?.activate()
          multiselect?.click()
        }
      }
    },
    customLabelSkin(skin: any): string {
      return String(skin.name)
    },
    onDragStart() {
      this.isDragging = true
    },
    onDragEnd() {
      this.isDragging = false
      this.data.forEach((item, index) => {
        item.key = index + 1
      })
    },
    setDataForTable() {
      const tempData = this.data
      this.data = []
      const limit = {
        min: 2,
        max: 24
      }
      this.form.column =
        this.form.column > limit.max
          ? limit.max
          : this.form.column < limit.min + 1
            ? limit.min + 1
            : this.form.column
      this.form.row =
        this.form.row > limit.max
          ? limit.max
          : this.form.row < limit.min
            ? limit.min
            : this.form.row
      const totalCells = this.form.column * this.form.row
      for (let i = 0; i < totalCells; i++) {
        if (tempData[i]?.id) {
          this.data.push(tempData[i])
        } else {
          this.data.push({
            key: i + 1,
            id: undefined,
            base: undefined,
            name: undefined,
            image: this.defaultSkinImage,
            position: undefined
          } as IRovSkinOnTable)
        }
      }
      this.selectSkinRovOnTable = this.data[0]
    },
    async saveTableAsImage() {
      if (!this.isSaving) {
        const element = document.getElementById('table-skin')
        if (element) {
          this.isSaving = true
          const originalData = [...this.data]
          this.data = this.data.map((item): void => {
            if (item.image && item.image.includes('?raw=true')) {
              const imagePath = item.image
                .replace(this.repoGitHubAssetsImagesSkin, '')
                .replace('?raw=true', '')
              return {
                ...item,
                image: require(`~/assets/images/skin/${imagePath}`)
              }
            }
            return item
          })

          await this.$nextTick()

          const canvas = await html2canvas(element, {
            backgroundColor: null,
            scale: 2
          })
          const image = canvas.toDataURL('image/png')
          const filename = `${this.timeStamp}-${this.fileNameSystem}.png`
          const link = document.createElement('a')
          link.href = image
          link.download = filename
          link.click()

          this.data = originalData
          this.isSaving = false
          this.saveDataToLocalStorage()
        }
      }
    },
    openClassSkinRovModal() {
      this.$bvModal.show('class-skin-rov-table')
    },
    onClickSelectSkinForSwap(item: IRovSkinOnTable) {
      this.selectSkinForSwap = item
    },
    onClickSwapSkinRov() {
      if (
        this.selectSkinForSwap.id &&
        this.selectSkinRovOnTable.id &&
        this.selectSkinForSwap.key !== this.selectSkinRovOnTable.key
      ) {
        const temp = { ...this.selectSkinRovOnTable }
        // Optimize swapping by finding indices once instead of forEach twice
        const selectedIndex = this.data.findIndex(
          item => item.key === this.selectSkinRovOnTable.key
        )
        const swapIndex = this.data.findIndex(
          item => item.key === this.selectSkinForSwap.key
        )

        if (selectedIndex !== -1) {
          this.data[selectedIndex].id = this.selectSkinForSwap.id
          this.data[selectedIndex].name = this.selectSkinForSwap.name
          this.data[selectedIndex].image = this.selectSkinForSwap.image
          this.data[selectedIndex].base = this.selectSkinForSwap.base
          this.data[selectedIndex].position = this.selectSkinForSwap.position
        }

        if (swapIndex !== -1) {
          this.data[swapIndex].id = temp.id
          this.data[swapIndex].name = temp.name
          this.data[swapIndex].image = temp.image
          this.data[swapIndex].base = temp.base
          this.data[swapIndex].position = temp.position
        }
        this.selectSkinForSwap = {} as IRovSkinOnTable
        this.selectSkinRovOnTable = {} as IRovSkinOnTable
      }
    },
    exportDataToFile() {
      const blob = new Blob([JSON.stringify(this.data, null, 2)], {
        type: 'application/json'
      })
      const link = document.createElement('a')
      link.href = URL.createObjectURL(blob)
      link.download = `${this.timeStamp}-${this.fileNameSystem}.json`
      link.click()
    },
    importDataFromFile(event: Event) {
      const target = event.target as HTMLInputElement
      if (!target.files?.length) {
        return
      }
      const file = target.files[0]
      const reader = new FileReader()
      reader.onload = (e) => {
        try {
          const json = JSON.parse(e.target?.result as string)
          if (Array.isArray(json)) {
            this.form.row = Math.ceil(json.length / this.form.column)
            this.data = json
            // Optimize position lookup with Map for better performance
            const skinMap = new Map()
            rov.forEach((skin) => {
              skinMap.set(skin.id, skin)
              skinMap.set(skin.name, skin)
              skinMap.set(skin.image, skin)
            })

            this.data.forEach((item) => {
              const skin =
                skinMap.get(item.id) ||
                skinMap.get(item.name) ||
                skinMap.get(item.image)
              if (skin) {
                item.position = skin.position
              }
            })
            this.selectSkinRovOnTable = this.data[0]
          } else {
            alert('ไฟล์ไม่ถูกต้อง')
          }
        } catch {
          alert('เกิดข้อผิดพลาดในการโหลดไฟล์')
        }
      }
      reader.readAsText(file)
      this.saveDataToLocalStorage()
    },
    onSelectSkinRovOnTable(item: IRovSkinOnTable) {
      if (!this.isDragging) {
        if (this.selectSkinRovOnTable.key === item.key) {
          this.selectSkinForSwap = item
        } else {
          this.selectSkinRovOnTable = item
          if (this.selectSkinForSwap.id) {
            this.onClickSwapSkinRov()
          }
        }
      }
    },
    onClickCancelSelectSkinRovSwap() {
      this.selectSkinForSwap = {} as IRovSkinOnTable
      this.selectSkinRovOnTable = this.data[0]
    },
    onClickResetDataSkinTable() {
      this.data = []
      this.setDataForTable()
      this.selectSkinRovOnTable = this.data[0]
      this.selectSkinForSwap = {} as IRovSkinOnTable
    },
    sortDataFollowPosition() {
      this.data.sort(
        (a, b) =>
          (a.position ? a.position : a.name ? 98 : 99) -
          (b.position ? b.position : b.name ? 98 : 99)
      )
    },
    resetDataSkinTable() {
      this.data = []
      this.saveDataToLocalStorage()
      setTimeout(() => {
        window.location.reload()
      }, 100)
    },
    applyGridDimensions() {
      this.form.column = this.formData.column
      this.form.row = this.formData.row
      this.form.width = this.formData.width
      this.setDataForTable()
    },
    toggleHeaderVisibility() {
      this.isHeaderVisible = !this.isHeaderVisible
      if (process.client && typeof window !== 'undefined') {
        localStorage.setItem(
          'rov-header-visible',
          this.isHeaderVisible.toString()
        )
      }
    },
    onRemoveSkinRov(item: IRovSkinOnTable) {
      this.data = this.data.filter(i => i.key !== item.key)
      this.setDataForTable()
    },
    saveDataToLocalStorage() {
      if (process.client && typeof window !== 'undefined') {
        localStorage.setItem(
          this.keyLocalStorage,
          JSON.stringify({
            data: this.data,
            form: this.form,
            timestamp: new Date().toISOString()
          })
        )
      }
    },
    loadDataFromLocalStorage() {
      if (process.client && typeof window !== 'undefined') {
        const storedData = localStorage.getItem(this.keyLocalStorage)
        if (storedData) {
          const parsedData = JSON.parse(storedData)
          // this.data = [[], ...parsedData.data] as IRovSkinOnTable[]
          const tempData = [] as IRovSkinOnTable[]
          parsedData.data.forEach((item: IRovSkinOnTable, index: number) => {
            if (item.name && item.image) {
              tempData.push({
                ...item,
                key: index // Ensure keys are sequential starting from 0
              })
            }
          })
          this.data = [...tempData] as IRovSkinOnTable[]
          this.formData = {
            ...parsedData.form
          } as {
            column: number;
            row: number;
            width: number;
          }
          this.form = {
            ...this.form,
            column: parsedData.form.column,
            row: parsedData.form.row,
            width: parsedData.form.width,
            isEnableItem: parsedData.form.isEnableItem
          } as {
            column: number;
            row: number;
            width: number;
            isEnableItem: boolean;
          }
        }
      }
      this.saveDataToLocalStorage()
    }
  }
})
</script>

<style scoped>
.option-with-image {
  display: flex;
  align-items: center;
}

.option-image {
  width: 35px;
  height: 35px;
  margin-right: 8px;
  border-radius: 4px;
  object-fit: cover;
}

.selected-tag {
  display: flex;
  align-items: center;
  background: #eee;
  padding: 2px 6px;
  border-radius: 3px;
  margin-right: 4px;
}

.tag-image {
  width: 10px;
  height: 20px;
  margin-right: 4px;
  border-radius: 3px;
  object-fit: cover;
}

.selected-tag button {
  border: none;
  background: transparent;
  cursor: pointer;
  padding: 0 4px;
  font-weight: bold;
  line-height: 1;
}

.cursor-pointer {
  cursor: pointer;
}

.skin-item {
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-sizing: border-box;
  position: relative;
}

.skin-item:hover {
  transform: scale(1.05);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  background-color: #f8f9fa;
  border-radius: 8px;
}

.skin-wrapper {
  position: relative;
  text-align: center;
}

.skin-future {
  position: absolute;
  bottom: 22%;
  left: 50%;
  transform: translateX(-50%);
  color: white;
  font-size: 80%;
  white-space: nowrap;
}

.skin-future-remove {
  position: absolute;
  top: -2px;
  left: -2px;
}

.drag-handle {
  position: absolute;
  top: 5px;
  right: 5px;
  opacity: 0.7;
  cursor: grab;
}

.drag-handle:hover {
  opacity: 1;
}

.grid-wrapper {
  display: grid;
  justify-content: center;
}

.skin-box {
  position: relative;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1040;
  width: 100vw;
  height: 100vh;
  background-color: none !important;
  opacity: 0.3 !important;
}

.ghost {
  opacity: 0.5;
  background: #c8ebfb;
  /* border: 2px dashed #007bff; */
  border-radius: 8px;
}

.chosen {
  opacity: 0.8;
  transform: scale(1.1);
  box-shadow: 0 4px 20px rgba(0, 123, 255, 0.5);
  border-radius: 8px;
}

.drag {
  opacity: 0.9;
  transform: rotate(5deg);
  transition: all 0.2s ease;
}

.sortable-fallback {
  opacity: 0;
}

.drag-handle {
  display: none;
}

/* Modern UI Styles */
.modern-bg {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  /* min-height: 100vh; */
}

.modern-container {
  /* backdrop-filter: blur(10px); */
  background: rgba(0, 0, 0, 0.4);
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.modern-btn {
  border: none;
  border-radius: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 12px 24px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
}

.modern-btn::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  transition: left 0.5s;
}

.modern-btn:hover::before {
  left: 100%;
}

.modern-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.modern-btn-primary {
  background: linear-gradient(45deg, #667eea, #764ba2);
}

.modern-btn-info {
  background: linear-gradient(45deg, #17a2b8, #138496);
}

.modern-btn-success {
  background: linear-gradient(45deg, #28a745, #20c997);
}

.modern-btn-warning {
  background: linear-gradient(45deg, #ffc107, #fd7e14);
}

.modern-btn-danger {
  background: linear-gradient(45deg, #dc3545, #c82333);
}

.modern-form-group label {
  font-weight: 600;
  color: #fff;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  margin-bottom: 8px;
}

.modern-input {
  border: none;
  border-radius: 10px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  color: #fff;
  font-weight: 500;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.modern-input:focus {
  background: rgba(255, 255, 255, 0.3);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1),
    0 0 0 3px rgba(102, 126, 234, 0.4);
  color: #fff;
}

.modern-input::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.modern-range {
  background: transparent;
}

.modern-range::-webkit-slider-track {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  height: 8px;
}

.modern-range::-webkit-slider-thumb {
  appearance: none;
  background: linear-gradient(45deg, #667eea, #764ba2);
  border-radius: 50%;
  height: 20px;
  width: 20px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.modern-switch .custom-control-input:checked ~ .custom-control-label::before {
  background: linear-gradient(45deg, #667eea, #764ba2);
  border-color: #667eea;
}

.modern-file-input .custom-file-label {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border: none;
  border-radius: 10px;
  color: #fff;
  font-weight: 500;
}

.modern-file-input .custom-file-input:focus ~ .custom-file-label {
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.4);
}

.modern-modal-header {
  background: linear-gradient(45deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.modern-title {
  font-weight: 700;
  font-size: 1.2em;
}

.modern-close-btn {
  color: #fff;
  font-size: 1.2em;
  transition: all 0.3s ease;
}

.modern-close-btn:hover {
  color: #ff6b6b;
  transform: scale(1.1);
}

/* iPad Optimized Styles */
.ipad-header-container {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.ipad-control-section {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(15px);
  border-radius: 16px;
  padding: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}

.section-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
}

.section-icon {
  font-size: 1.4rem;
  margin-right: 12px;
  color: #667eea;
}

.section-title {
  margin: 0;
  font-weight: 600;
  color: #fff;
  font-size: 1.1rem;
}

/* Grid Controls */
.ipad-grid-controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 12px;
  align-items: end;
}

.grid-input-group {
  min-width: 120px;
}

.grid-apply-btn {
  grid-column: span 2;
}

.ipad-form-group {
  margin-bottom: 4px;
}

.ipad-form-group label {
  font-size: 0.85rem;
  margin-bottom: 4px;
  font-weight: 500;
  padding: 0;
}

.ipad-input {
  height: 48px;
  font-size: 16px;
  border-radius: 12px;
  padding: 12px 16px;
}

.ipad-range {
  height: 36px;
  margin-top: 2px;
  margin-bottom: 0;
}

.ipad-range::-webkit-slider-track {
  height: 10px;
  border-radius: 12px;
}

.ipad-range::-webkit-slider-thumb {
  height: 24px;
  width: 24px;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.4);
}

.ipad-primary-btn {
  height: 52px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 14px;
  width: 100%;
  min-height: 52px;
}

/* Settings Row */
.ipad-settings-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
}

.setting-item {
  flex: 1;
}

.action-buttons {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.ipad-switch {
  transform: scale(1.3);
  margin-top: 8px;
}

.ipad-action-btn {
  height: 48px;
  font-size: 15px;
  padding: 12px 20px;
  border-radius: 12px;
  min-width: 140px;
}

/* File Controls */
.ipad-file-controls {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

.file-input-wrapper {
  width: 100%;
}

.ipad-file-input {
  width: 100%;
}

.ipad-file-input .custom-file-label {
  height: 48px;
  line-height: 2.2;
  font-size: 15px;
  border-radius: 12px;
  padding: 8px 16px;
}

.file-action-buttons {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.ipad-file-btn {
  height: 48px;
  font-size: 15px;
  border-radius: 12px;
  padding: 12px 16px;
}

/* Responsive Design for iPad */
@media screen and (min-width: 768px) and (max-width: 1024px) {
  .ipad-header-container {
    max-width: 100%;
  }

  .ipad-grid-controls {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }

  .grid-apply-btn {
    grid-column: span 2;
  }

  .ipad-settings-row {
    flex-direction: column;
    align-items: stretch;
    gap: 16px;
  }

  .action-buttons {
    justify-content: center;
  }

  .file-action-buttons {
    grid-template-columns: 1fr;
    gap: 12px;
  }
}

@media screen and (min-width: 1024px) {
  .ipad-grid-controls {
    grid-template-columns: repeat(4, 1fr);
  }

  .grid-apply-btn {
    grid-column: span 1;
  }

  .file-action-buttons {
    grid-template-columns: 1fr 1fr;
  }
}

/* Touch-friendly improvements */
@media (hover: none) {
  .ipad-input:focus,
  .ipad-range:focus {
    outline: 3px solid rgba(102, 126, 234, 0.6);
    outline-offset: 2px;
  }

  .modern-btn:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }
}

/* Header Toggle Styles */
.header-toggle-section {
  display: flex;
  justify-content: center;
  align-items: center;
}

.header-toggle-btn {
  border: 2px solid rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 50px;
  padding: 12px 24px;
  font-weight: 600;
  color: #fff;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
  min-height: 48px;
  font-size: 15px;
}

.header-toggle-btn::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  transition: left 0.5s;
}

.header-toggle-btn:hover {
  border-color: rgba(255, 255, 255, 0.5);
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  color: #fff;
}

.header-toggle-btn:hover::before {
  left: 100%;
}

.header-toggle-btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.header-toggle-btn:focus {
  border-color: rgba(102, 126, 234, 0.6);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), 0 0 0 3px rgba(102, 126, 234, 0.3);
}

/* Collapse Animation Enhancement */
.ipad-header-container.collapse:not(.show) {
  opacity: 0;
  transform: translateY(-20px);
}

.ipad-header-container.collapse.show {
  opacity: 1;
  transform: translateY(0);
}

.ipad-header-container.collapsing {
  transition: height 0.35s ease-out, opacity 0.35s ease-out,
    transform 0.35s ease-out;
}

/* Compact Header Section */
.compact-header-section {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
}

.compact-toggle-btn,
.compact-reset-btn,
.compact-facebook-btn,
.compact-toggle-item {
  border-radius: 20px;
  font-weight: 500;
  font-size: 13px;
  padding: 6px 16px;
  min-height: 32px;
  border-width: 1.5px;
  backdrop-filter: blur(8px);
  transition: all 0.25s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.compact-toggle-btn {
  border-color: rgba(255, 255, 255, 0.4);
  background: rgba(255, 255, 255, 0.12);
  color: #fff;
}

.compact-toggle-btn:hover {
  border-color: rgba(255, 255, 255, 0.6);
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}

.compact-reset-btn {
  background: linear-gradient(45deg, #dc3545, #c82333);
  border-color: #dc3545;
  color: #fff;
}

.compact-reset-btn:hover:not(:disabled) {
  background: linear-gradient(45deg, #c82333, #a71e2a);
  border-color: #bd2130;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.4);
}

.compact-reset-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.compact-toggle-item {
  border-color: rgba(108, 117, 125, 0.4);
  background: rgba(108, 117, 125, 0.12);
  color: #fff;
}

.compact-toggle-item:hover {
  border-color: rgba(108, 117, 125, 0.6);
  background: rgba(108, 117, 125, 0.2);
  color: #fff;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}

.compact-toggle-item.btn-success {
  border-color: #6f42c1;
  background: linear-gradient(45deg, #6f42c1, #8e44ad);
}

.compact-toggle-item.btn-success:hover {
  border-color: #5a2d91;
  background: linear-gradient(45deg, #5a2d91, #7d3c98);
  box-shadow: 0 4px 12px rgba(111, 66, 193, 0.4);
}

.compact-facebook-btn {
  background: linear-gradient(45deg, #3b5998, #8b9dc3);
  border-color: #3b5998;
  color: #fff;
}

.compact-facebook-btn:hover {
  background: linear-gradient(45deg, #8b9dc3, #3b5998);
  border-color: #3b5998;
  box-shadow: 0 4px 12px rgba(59, 89, 152, 0.4);
}

.fit-col-image {
  width: 100%;
  max-height: 8.5vh;
  border-radius: 8px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  object-fit: cover;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}
</style>

<style>
legend.bv-no-focus-ring.col-form-label {
  white-space: nowrap !important;
}
</style>
