import { styles } from "../Pages/Homepage.styles";

export interface RewardProps {
    classes: {
        [X in keyof (typeof styles)]: string;
      };
};

export interface VideoListType {
    _id: string;
    youtube_id: string;
    title: string;
    description: string;
    published_at: string;
    thumbnail: {
        default_res: string;
        high_res: string;
    }
}