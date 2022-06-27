import * as React from 'react';
import withStyles from 'react-jss';
import { styles } from './Header.styles';

interface RewardProps {
    classes: {
        [X in keyof (typeof styles)]: string;
      };
};

const Header = (props: RewardProps) => {
    
    const {classes} = props;

    return (
        <nav className={classes.Header}>
            FamPay Backend Intern Assignment
            <br/>
        </nav>
    )
}
export default withStyles(styles)(Header);