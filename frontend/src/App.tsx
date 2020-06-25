import React from 'react';
import './App.css';
import { Home } from './components/Home';
import { AddUser } from './components/AddUser';
import { EditUser } from './components/EditUser';
import { UsersList } from './components/UsersList';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {
  return (
    <div style={{ maxWidth: "30rem", margin: "4rem auto" }}>
      <Router>
        <Switch>
          <Route exact path='/' component={Home}/>
          <Route exact path='/clientes' component={UsersList}/>
          <Route path='/clientes/add' component={AddUser}/>
          <Route path='/clientes/edit/:id' component={EditUser}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
