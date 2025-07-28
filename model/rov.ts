export interface IRovSkin {
    id: number;
    base?: string;
    name?: string;
    image: string;
    position?: number;
}

export interface IRovSkinOnTable extends IRovSkin {
    key: number;
}
