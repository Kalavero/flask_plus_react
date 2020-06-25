import React, { createContext, useReducer } from 'react'
import AddReducer from './AppReducer';

const initialState = {
  users: [
    {id:1, first_name: 'Andre', last_name: 'Souza', 'test@example.com'},
    {id:2, first_name: 'Bill', last_name: 'Cosby', 'bc@example.com'}
  ]
}
