import { Table, TableContainer, TableHead, TableBody, TableRow, TableCell, Paper } from '@mui/material';

const TruthTable = (props) => {

    const VariableColumns = props.Term.termData.variables.map((term, key) => {

        return (<TableCell key={key}> {term} </TableCell>)

    })


    const rowDataValues = Object.values(props.Term.termData.rowData)

    const Rows = rowDataValues.map((row, key) => {
        
        const rowItemValues = Object.values(row)
        console.log(key)

        const RowItems = rowItemValues.map((rowItem, key) => {
            return <TableCell key={key} >{rowItem}</TableCell>
        })

        return <TableRow key={key} >{RowItems}</TableRow>
    })

    // console.log(Rows)

    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        {VariableColumns}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {/* {rows.map((row) => (
                        <TableRow
                            key={row.name}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {row.name}
                            </TableCell>
                            <TableCell align="right">{row.calories}</TableCell>
                            <TableCell align="right">{row.fat}</TableCell>
                            <TableCell align="right">{row.carbs}</TableCell>
                            <TableCell align="right">{row.protein}</TableCell>
                        </TableRow>
                    ))} */}
                {Rows}
                </TableBody>
            </Table>
        </TableContainer>
    )

}


export default TruthTable