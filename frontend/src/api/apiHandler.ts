import apiProvider from './provider';
import { getErrorMessage } from './utils';

export const GET = async (
    url: string,
    params?: any,
  ): Promise<any> => {
    try {
        const response = await apiProvider.get(url, {
          params
        });
        return {
          isSuccess: true,
          data: response
        };
      } catch (err) {
        const errorMessage = getErrorMessage(err);
        return {
          errorMessage,
          isSuccess: false
        };
      }
}