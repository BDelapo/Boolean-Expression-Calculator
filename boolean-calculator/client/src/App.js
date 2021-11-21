import './App.css';
import { Box, Grid, Container, TextField } from '@mui/material';
import React, { useState, useEffect } from 'react';
import Table from './Table'
import axios from 'axios'

const ID = Math.floor(Math.random()*20)


function App() {
  const [inputTerm, setInputTerm] = useState('')
  const [separatedTerm, setSeparatedTerm] = useState([])

  const toObject = term =>{
    var obj = {}
    for(var i = 0; i < term.length; i++){
      obj[i] = term[i]
    }
    return obj
  }


//   const getRows = async (ID, input) => {
//     await axios.post('http://127.0.0.1:5000/calculator', {
//       id : ID,
//       terms : input
//     }).then(function (response) {
//       console.log(response);
//     }).catch(function (error) {
//       console.log(error);
//     })
    
//     axios.get('http://127.0.0.1:5000/calculator', {params: {
//       id: ID
//     }})
//     .then((response) => {
//       console.log(response.data);
//   })
// }

  const onChange = e => {
    var input = e.target.value
    var separatedInput = input.split(/([+*-])/)
    setInputTerm(input)
    setSeparatedTerm(separatedInput)
    // console.log(separatedInput.length)
    // var inputObj = toObject(separatedInput)
    // console.log(inputObj)
    // getRows(ID, inputObj)
    
  }



  return (
    <div className="App">
      <Box sx={{ height: '100vh', display: 'flex', alignItems: 'center' }}>
        <Grid container spacing={0}>
          <Grid item xs={12}>
            <Container maxWidth="sm">
              <TextField id="outlined-basic" label="Outlined" variant="outlined" onChange={e => onChange(e)} value={inputTerm} />
            </Container>
          </Grid>
          <Grid item xs={12}>
            <Container maxWidth="sm">
              <Table Term={{ separatedTerm }} />
            </Container>
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default App;
