import * as React from 'react';
import { useState, useEffect } from 'react';
import { styles } from './Homepage.styles';
import withStyles from 'react-jss';
import Header from '../components/Header';
import {Button, Input, message} from 'antd';
import { SearchOutlined, RightOutlined } from '@ant-design/icons';
import { fetchVideos } from '../api/apis';
import VideoCard from '../components/VideoCard';
import { RewardProps, VideoListType } from '../lib/Types';

const Homepage = (props: RewardProps) => {

    const { classes } = props;
    const { Search } = Input;

    const [state, setState] = useState({
        query: "" as string,
        result: [] as any,
        currentPage: 0 as number,
    });

    const updateQuery = (value: string) => {
        setState({
            ...state,
            query: value
        });
    };
    const updatePage = (newPage: number) => {
        console.log("[Website]: Updating Page...", newPage);
        setState({
            ...state,
            currentPage: newPage
        });
        getVideos(newPage);
    };
    const getVideos = async (pageNumber: number) => {
        const api_results = await fetchVideos({
            'page': pageNumber ?? state.currentPage,
            'query': state.query
        });
        if(api_results?.isSuccess){
            const videoCards = api_results?.data.map( (videoElement: VideoListType) => {
                return <VideoCard
                    key = {videoElement?.youtube_id}
                    title = {videoElement?.title}
                    description = {videoElement.description}
                    thumbnail_default_res = {videoElement.thumbnail.default_res}
                    thumbnail_high_res = {videoElement.thumbnail.high_res}
                />
            });
            if(videoCards.length > 0){
                console.log("[Website] New Videos Fetched");
                setState({
                    ...state,
                    result: videoCards
                });
            }
            else{
                message.error("No Videos Found");
            };
        } else {
            message.error(api_results?.errorMessage);
        }
    };

    useEffect(() => {
        getVideos(0);
    }, []);

    return (
        <div className={classes.mainDiv}>
            <Header />

            <div className={classes.searchDiv}>
                <Search
                    placeholder='Search Football Videos'
                    className={classes.search}
                    value={state.query}
                    allowClear={true}
                    onSearch={(value: string) => {updateQuery(value)}}
                />
            </div>
            <Button
                className={classes.searchButton}
                shape="circle"
                icon={<SearchOutlined />}
                onClick={() => getVideos(0)}
            />

            <div className={classes.videoHolder}>
                {state.result}
            </div>

            <div className={classes.pagination}>
                <Button
                    shape='circle'
                    icon={<RightOutlined />}
                    onClick={() => updatePage(state.currentPage+1)}
                />
            </div>


        </div>
    );
}

export default withStyles(styles)(Homepage);