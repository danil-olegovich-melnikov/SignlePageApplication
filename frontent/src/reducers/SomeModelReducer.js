import {DELETE_SOME_MODEL, LIST_SOME_MODEL, UPDATE_SOME_MODEL,} from "../actions/types";

const INITIAL_STATE = {
    instances: {
        "total": 0,
        "results": [],
    }
};

const reducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case LIST_SOME_MODEL:
            return {
                ...state, instances: action.payload
            }

        case UPDATE_SOME_MODEL:
            return {
                ...state,
                instances: [...state.instances, ...action.payload.instance],
            };
        case DELETE_SOME_MODEL:
            return {
                ...state, instances: state.instances.filter(instance => {
                    return instance.id !== action.payload.id
                })
            };
        default:
            return state
    }
};

export default reducer