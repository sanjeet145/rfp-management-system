import TextField from "@mui/material/TextField";


export default function InputBox({label="Type here..", placeholder, func}){
    return (
        <TextField
          id="outlined-multiline-static"
          label={label}
          placeholder={placeholder}
          multiline
          maxRows={4}
          onChange={func}
        />
    )
}