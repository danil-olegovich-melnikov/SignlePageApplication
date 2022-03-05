import {
    LIST_SOME_MODEL,
    DELETE_SOME_MODEL,
    UPDATE_SOME_MODEL,
} from './types';


export const list_some_model = (instances) => {
    return {
        type: LIST_SOME_MODEL,
        payload: instances
    }
};


export const delete_some_model = (id) => {
    return {
        type: DELETE_SOME_MODEL,
        payload: {
            'id': id,
        }
    }
}

export const update_some_model = (data) => {
    return {
        type: UPDATE_SOME_MODEL,
        payload: data,
    }
}