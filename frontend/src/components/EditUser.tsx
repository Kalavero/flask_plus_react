import React from 'react';
import { Link } from 'react-router-dom';
import {
  Form,
  FormGroup,
  Label,
  Input,
  Button
} from 'reactstrap';


export const EditUser = () => {
  return (
    <div>
      <h1> Editar Cliente </h1>
      <Form>
        <FormGroup>
          <Label>Nome</Label>
          <Input type="text" placeholder="Insira o nome"></Input>
          <Label >Sobrenome</Label>
          <Input type="tex" placeholder="Insira o sobrenome"></Input>
          <Label>Email</Label>
          <Input type="email" placeholder="Insira o email"></Input>
        </FormGroup>
        <Button type="submit" className="btn btn-primary">Enviar</Button>
        <Link to="/" className="btn btn-danger ml-2">Voltar</Link>
      </Form>
    </div>
  )
}
