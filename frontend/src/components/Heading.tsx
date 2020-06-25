import React from 'react';
import { Link } from 'react-router-dom';
import {
  Navbar,
  Nav,
  NavItem,
  NavbarBrand,
  Container
} from 'reactstrap';

export const Heading = () => {
  return (
    <Navbar color="dark" dark>
      <Container>
        <NavbarBrand href="/clientes">Clientes</NavbarBrand>
        <Nav>
          <NavItem>
            <Link to="/clientes/add" className="btn btn-primary"> Cadastrar usuário </Link>
          </NavItem>
        </Nav>
      </Container>
    </Navbar>
  )
}
