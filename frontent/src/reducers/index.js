import {combineReducers} from "redux";
import SomeModelReducer from "./SomeModelReducer";

export default combineReducers({
    some_model: SomeModelReducer,
})