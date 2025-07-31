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
          <div class="w-100 font-size-18 d-block d-flex align-items-center">
            <b-icon icon="trophy" class="mr-2" />
            <span>ข้อมูลระดับ</span>
          </div>
          <fa-icon
            icon="close"
            class="me-1 cursor-pointer"
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
    <div class="bg-dark" style="min-height: 100vh">
      <div class="container-fluid py-3 text-white">
        <b-row>
          <b-col cols="2">
            <b-form-group label="แนวนอน (Row)">
              <b-form-input
                v-model="form.column"
                type="number"
                placeholder="ตัวอย่าง : 3 - 12"
              />
            </b-form-group>
          </b-col>

          <b-col cols="2">
            <b-form-group label="แนวตั้ง (Column)">
              <b-form-input
                v-model="form.row"
                type="number"
                placeholder="ตัวอย่าง : 3 - 12"
              />
            </b-form-group>
          </b-col>

          <b-col cols="3">
            <b-form-group :label="`ความกว้าง (${form.width}%)`">
              <b-form-input
                v-model="form.width"
                type="range"
                :step="3"
                class="w-100 h-100"
              />
            </b-form-group>
          </b-col>

          <b-col cols="1">
            <b-form-group label="ชื่อตัวหลัก">
              <b-form-checkbox
                v-model="form.isEnableItem"
                switch
                class="mt-2"
              />
            </b-form-group>
          </b-col>

          <b-col cols="4">
            <div class="d-flex">
              <b-form-file
                class="mt-2 mr-2"
                accept=".json"
                browse-text="Import"
                :placeholder="`data.json`"
                @change="importDataFromFile"
              >
                <template #file-name>
                  <b-icon icon="file-earmark-arrow-up" class="mr-2" />
                  เลือกไฟล์
                </template>
              </b-form-file>

              <b-button
                class="w-75 mt-2"
                variant="primary"
                @click="exportDataToFile"
              >
                <b-icon icon="file-earmark-arrow-down" class="mr-2" /> บันทึก
                JSON
              </b-button>
            </div>

            <div class="d-flex">
              <b-button
                class="w-100 mt-2 mr-2"
                variant="info"
                @click="openClassSkinRovModal"
              >
                <b-icon icon="Trophy" class="mr-2" /> ข้อมูลระดับ
              </b-button>

              <b-button
                class="w-100 mt-2"
                variant="success"
                @click="saveTableAsImage"
              >
                <b-icon icon="image" class="mr-2" /> บันทึกรูปภาพ
              </b-button>
            </div>
          </b-col>
        </b-row>

        <b-row>
          <b-col cols="6">
            <b-form-group
              :label="`กำลังเลือก : ${selectSkinRovOnTable.key || 0} -  ${
                !selectSkinRovOnTable?.name
                  ? 'ว่าง'
                  : selectSkinRovOnTable?.name
              }`"
            >
              <Multiselect
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
                    <img :src="option.image" alt="icon" class="option-image">
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
                    <img :src="option.image" alt="icon" class="tag-image">
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
          <b-col cols="3" class="d-flex align-items-center">
            <b-button
              class="w-100 mt-4"
              variant="warning"
              @click="sortDataFollowPosition"
            >
              <b-icon icon="sort-numeric-down" class="mr-2" />
              เรียงสกิน ROV ตามข้อมูล Class
            </b-button>
          </b-col>
          <b-col cols="3" class="d-flex align-items-center">
            <b-button
              class="w-100 mt-4"
              variant="danger"
              @click="resetDataSkinTable"
            >
              <b-icon icon="sort-numeric-down" class="mr-2" />
              เริ่มต้นใหม่
            </b-button>
          </b-col>
        </b-row>
      </div>

      <div class="d-flex justify-content-center">
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
              v-for="item in data.slice(0, form.row * form.column)"
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
                <div v-if="item.base && form.isEnableItem" class="skin-future">
                  <div class="d-flex">
                    <!-- {{ item.base }} -->
                    {{ item.position }}
                    <!-- {{ item.id }} -->
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
      selectSkinRov: [] as IRovSkin[],
      selectSkinRovOnTable: {} as IRovSkinOnTable,
      selectSkinForSwap: {} as IRovSkinOnTable,
      rov: rov as IRovSkin[],
      isDragging: false,
      form: {
        column: 15,
        row: 5,
        width: 60,
        isEnableItem: false
      } as {
        column: number;
        row: number;
        width: number;
        isEnableItem: boolean;
      },
      data: [] as IRovSkinOnTable[],
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
    defaultSkinImage() {
      return require('~/assets/images/skin/default.jpeg')
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
      return this.form.width * 1.8
    }
  },
  watch: {
    'form.column'() {
      this.setDataForTable()
    },
    'form.row'() {
      this.setDataForTable()
    },
    selectSkinRov(val: IRovSkin) {
      if (val) {
        this.selectSkinRovOnTable = {
          ...this.selectSkinRovOnTable,
          ...val
        }
        this.data.forEach((item) => {
          if (item.key === this.selectSkinRovOnTable.key) {
            item.id = this.selectSkinRovOnTable.id
            item.name = this.selectSkinRovOnTable.name
            item.image = this.selectSkinRovOnTable.image
            item.base = this.selectSkinRovOnTable.base
            item.position = this.selectSkinRovOnTable.position
          }
        })
        this.selectSkinRov = undefined
        if (this.selectSkinRovOnTable.key < this.form.row * this.form.column) {
          this.selectSkinRovOnTable = {
            ...this.selectSkinRovOnTable,
            ...{
              key: this.selectSkinRovOnTable.key + 1,
              id: undefined,
              name: undefined,
              base: undefined,
              image: this.defaultSkinImage,
              position: undefined
            }
          } as IRovSkinOnTable
        }
      }
    },
    data: {
      handler() {
        // อัพเดท key ให้ตรงกับ index ใหม่หลังจากการลาก
        this.data.forEach((item, index) => {
          item.key = index + 1
        })
      },
      deep: true
    }
  },
  created() {
    this.setDataForTable()
  },
  methods: {
    customLabelSkin(skin: any): string {
      return String(skin.name)
    },
    onDragStart() {
      this.isDragging = true
    },
    onDragEnd() {
      this.isDragging = false
      // อัพเดท key หลังจากการลากเสร็จ
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
      const element = document.getElementById('table-skin')
      if (!element) {
        return
      }
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
        this.data.forEach((item) => {
          if (item.key === this.selectSkinRovOnTable.key) {
            item.id = this.selectSkinForSwap.id
            item.name = this.selectSkinForSwap.name
            item.image = this.selectSkinForSwap.image
            item.base = this.selectSkinForSwap.base
            item.position = this.selectSkinForSwap.position
          }
        })
        this.data.forEach((item) => {
          if (item.key === this.selectSkinForSwap.key) {
            item.id = temp.id
            item.name = temp.name
            item.image = temp.image
            item.base = temp.base
            item.position = temp.position
          }
        })
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
            this.data.forEach((item) => {
              rov.find((skin) => {
                if (skin.id === item.id) {
                  item.position = skin.position
                  return true
                }
                return false
              })
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
      this.data.sort((a, b) => (a.position ?? 99) - (b.position ?? 99))
    },
    resetDataSkinTable() {
      this.data = []
      this.setDataForTable()
      this.selectSkinRovOnTable = this.data[0]
      this.selectSkinForSwap = {} as IRovSkinOnTable
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
</style>
