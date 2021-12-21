import { Table, TableContainer, TableHead, TableBody, TableRow, TableCell, Paper } from '@mui/material';


const TruthTable = (props) => {

    const VariableColumns = props.Term.termData.variables.map((term, key) => {
        return (<TableCell align="center" sx={{ width: 30 }} key={key}> {term} </TableCell>)
    })

    const rowDataValues = Object.values(props.Term.termData.rowData)

    const Rows = rowDataValues.map((row, key) => {
        const rowItemValues = Object.values(row)
        const RowItems = rowItemValues.map((rowItem, key) => {
            return <TableCell align="center" sx={{ width: 30 }} key={key} >{rowItem}</TableCell>
        })
        return <TableRow key={key} >{RowItems}</TableRow>
    })

    return (
        <Paper sx={{ width: "100%", overflow: "hidden" }}>
            <TableContainer sx={{ maxHeight: "70vh" }}>
                <Table sx={{ minWidth: "650px" }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            {VariableColumns}
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {Rows}
                    </TableBody>
                </Table>
            </TableContainer>
        </Paper>
    )

}


export default TruthTable