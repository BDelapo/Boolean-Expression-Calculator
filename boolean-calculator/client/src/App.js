import './App.css';
import { Box, Grid, Container, TextField } from '@mui/material';
import React, { useState, useEffect } from 'react';
import Table from './Table'
import axios from 'axios'

axios.defaults.withCredentials = true


function App() {
  const [inputTerm, setInputTerm] = useState('')
  const [separatedTerm, setSeparatedTerm] = useState([])

  useEffect(() => {
    sendSessionId()
  }, [])


  const toObject = term => {
    var obj = {}
    for (var i = 0; i < term.length; i++) {
      obj[i] = term[i]
    }
    return obj
  }

  const sendSessionId = async () => {
    await axios.post('http://127.0.0.1:8000/api/set-session/', {
    }).then(function (response) {
      console.log(response)
    }).catch(function (error) {
      console.log(error);
    })
  }

  const postRows = async (input) => {
    await axios.post('http://127.0.0.1:8000/api/set-session/calculate/', {
      term: input
    }).then(function (response) {
      console.log(response)
    }).catch(function (error) {
      console.log(error);
    })
  
  }

  const getRows = async () => {
    await axios.get('http://127.0.0.1:8000/api/set-session/calculate/', {
    }).then(function (response) {
      console.log(response);
    }).catch(function (error) {
      console.log(error);
    })
  }

  const onChange = e => {
    var input = e.target.value
    var separatedInput = input.split(/([+*-])/)
    var inputObj = toObject(separatedInput)
    setInputTerm(input)
    setSeparatedTerm(separatedInput)
    postRows(inputObj)
    getRows()
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
