import React, {useState} from "react";

import Classe from "./Components/Classe";
import ListaArquivo from "./Components/Lista_arquivo";
import Resultado from "./Components/Resultados";
import Titulo from "./Components/Titulo"
import FileUpload from "./Components/FileUpload";
import FileList from "./Components/FileList";

import './App.css'

export default function App() {
  const [files, setFiles] = useState([]);

  const removeFile = (filename) => {
    setFiles(files.filter((file) => file.name !== filename));
  };

  return (
    <div className="first">
      <div className="container">
        <Titulo />
        <Classe />
        <ListaArquivo />
        {/* <Resultado /> */}
        <FileUpload files={files} setFiles={setFiles} removeFile={removeFile} />
        <FileList files={files} removeFile={removeFile} />
      </div>
    </div>
  );
}
