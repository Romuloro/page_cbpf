import React from "react";

const ListaArquivo = () => {
  return (
    <div>
        <label for="avatar">Choose a profile picture:</label>

        <input type="file"
            id="avatar"
            name="avatar"
            multiple="true"
            accept="image/png, image/jpeg"
        />

        <button>Upload</button>  
    </div>
  );
};

export default ListaArquivo;
