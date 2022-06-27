export const styles = {
    mainDiv: {
        textAlign: "center",
        minHeight: "100vh",
        display: "flex",
        width: "100vw",
        alignItems: "center",
        flexDirection: "column",
        backgroundColor: "#FFFFFF",
        paddingBottom: "5vh",
    },

    searchDiv: {
        marginTop: "30px",
        paddingLeft: "5vw",
        paddingRight: "5vw",
        display: "flex",
        gap: "1vw",
    },

    search: {
        '& .ant-input-search': {
            width: "100%",
            backgroundColor: "#FFAD00",
            padding: "0.5vw",
            borderRadius: "20px",
            border: "none",
            outline: "none",
            fontSize: "large",
            color: "#000000",
        },
    },

    videoHolder: {
        color: "aliceblue",
        paddingLeft: "5vw",
        paddingRight: "5vw",
        paddingBottom: "5vh",
        marginTop: "30px",
        display: "flex",
        justifyContent: "space-around",
        flexWrap: "wrap",
        gap: "1vw",
    },

    pagination: {
        display: "flex",
        gap: "10px"
    }
};