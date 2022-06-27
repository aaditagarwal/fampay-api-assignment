export const getErrorMessage = (err: any) => {
    let errorMessage = '';
    if (!err.response) {
      errorMessage = 'Could not connect. Please check your internet connection';
    } else {
      const responseData = err.response.data;
      if (responseData && responseData.error) {
        errorMessage =
          Object.prototype.toString.call(responseData.error.message) ===
          '[object Object]'
            ? responseData.error.message.message
            : responseData.error.message;
      } else {
        errorMessage = `Something went wrong\n${err.message}`;
      }
    }
    return errorMessage;
};  