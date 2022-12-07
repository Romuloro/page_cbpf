import React from "react";

import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";


import './Classe.css'

const Classe = () => {
  return (
    <div className="container_radio">
      <FormGroup>
        <FormControlLabel
          control={<Checkbox/>}
          label="Valor 1"
          value={"valor 1"}
        />
        <FormControlLabel
          control={<Checkbox/>}
          label="Valor 2"
          value={"valor 2"}
        />
        <FormControlLabel
          control={<Checkbox/>}
          label="Valor 3"
          value={"valor 3"}
        />
      </FormGroup>
    </div>
  );
};

export default Classe;
