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

    const [query, setQuery] = useState("" as string);
    const [result, setResult] = useState([] as any);
    const [currentPage, setCurrentPage] = useState(0 as number);

    const updatePage = (newPage: number) => {
        console.log("[Website]: Updating Page...", newPage);
        setCurrentPage(newPage);
        getVideos(newPage);
    };
    const getVideos = async (pageNumber: number) => {
        const api_results = await fetchVideos({
            'page': pageNumber ?? currentPage,
            'query': query
        });
        if(api_results?.isSuccess){
            if(api_results?.data?.length > 0){
                console.log("[Website] New Videos Fetched");
                setResult([]);
                setResult(api_results?.data);
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
                <Input
                    placeholder='Search Football Videos'
                    className={classes.search}
                    value={query}
                    allowClear={true}
                    onChange={(event) => setQuery(event.target.value)}
                />
                <Button
                    shape='circle'
                    icon={<SearchOutlined />}
                    onClick={() => getVideos(0)}
                />
            </div>

            <div className={classes.videoHolder}>
                {result.map((videoElement: VideoListType) => <VideoCard
                    key = {videoElement?.youtube_id}
                    title = {videoElement?.title}
                    description = {videoElement.description}
                    thumbnail_default_res = {videoElement.thumbnail.default_res}
                    thumbnail_high_res = {videoElement.thumbnail.high_res}
                />)}
            </div>

            <div className={classes.pagination}>
                <Button
                    shape='circle'
                    icon={<RightOutlined />}
                    onClick={() => updatePage(currentPage+1)}
                />
            </div>
        </div>
    );
}

export default withStyles(styles)(Homepage);