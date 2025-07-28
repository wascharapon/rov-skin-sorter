export interface IRovSkin {
    id: number;
    base?: string;
    name?: string;
    image: string;
}

export interface IRovSkinOnTable extends IRovSkin {
    key: number;
}
