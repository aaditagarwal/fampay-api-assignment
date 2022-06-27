import * as React from 'react';
import withStyles from 'react-jss';
import { styles } from './Videocard.styles';

interface VideoCardType{
    classes: {
        [X in keyof (typeof styles)]: string;
    };
    title: string;
    description: string;
    thumbnail_default_res: string;
    thumbnail_high_res: string;
};

const Videocard = (props: VideoCardType) => {

    const { classes, title, description, thumbnail_default_res, thumbnail_high_res } = props;

    return(
        <div className={classes.card}>
            
            <div className={classes.thumbnail}>
                <img alt={title} src={thumbnail_high_res}/>
            </div>

            <div className={classes.content}>
                <h3 className={classes.title}>{title}</h3>
                <p className={classes.description}>{description}</p>
            </div>

        </div>
    );
};

export default withStyles(styles)(Videocard);