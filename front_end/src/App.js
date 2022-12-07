import React from "react";

import Classe from "./Components/Classe";
import ListaArquivo from "./Components/Lista_arquivo";
import Resultado from "./Components/Resultados";
import Titulo from "./Components/Titulo"

import './App.css'

export default function App() {
  return (
    <div className="first">
      <div className="container">
        <Titulo/>
        <Classe/>
        <ListaArquivo/>
        <Resultado/>
      </div>
    </div>
  );
}
