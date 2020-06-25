import React from 'react';
import { Link } from 'react-router-dom';
import {
  ListGroup,
  ListGroupItem,
  Button
} from 'reactstrap';

export const UsersList = () => {
  return (
    <ListGroup className="mt-4">
      <ListGroupItem className="d-flex">
        <strong>User one</strong>
        <div className="ml-auto">
          <Link to="/clientes/edit" className="btn btn-secondary mr-2"> Editar </Link>
          <Button type="submit" className="btn btn-danger"> Excluir </Button>
        </div>
      </ListGroupItem>
    </ListGroup>
  )
}
