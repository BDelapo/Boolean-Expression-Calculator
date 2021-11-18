import './App.css';
import { Box, Grid, Container, TextField } from '@mui/material';
import React, { useState, useEffect } from 'react';
import Table from './Table'





function App() {
  const [inputTerm, setInputTerm] = useState('')
  const [separatedTerm, setSeparatedTerm] = useState([])

  const onChange = e => {
    setInputTerm(e.target.value)
    setSeparatedTerm(e.target.value.split(/([+*\/-])/))
    console.log(separatedTerm.length)
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
