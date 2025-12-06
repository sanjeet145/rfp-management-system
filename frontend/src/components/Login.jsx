import { useState } from "react"
import { login } from "../utils/api"
import { Box, Card, CardContent, Grid } from "@mui/material"
import InputBox from "../utils/Input"
import IconButton from "../utils/IconButton"
import LoginIcon from "@mui/icons-material/Login"
import { useNavigate } from "react-router-dom"


export default function Login() {
    const [email, setEmail] = useState("")
    const navigate = useNavigate()
    const handleLogin = async (e) => {
        e.preventDefault()
        if (email.trim() === "") {
            return alert("enter valid email")
        }
        const res = await login({"email":email})
        if (res["status"] === 200) {
            navigate('/')
        }
    }
    return (
        <>
            <Box sx={{ flexGrow: 1, padding: 2 }}>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <Card sx={{ height: "100%", boxShadow: "0px 1px 1px black" }}>
                        <CardContent sx={{ height: "100%", display: "flex", flexDirection: "column", gap: "5px" }}>
                            <InputBox placeholder={"Enter your email"} label="Email" func={(e) => { setEmail(e.target.value) }}>
                            </InputBox>
                            <IconButton name={"Login"} func={handleLogin} icon={<LoginIcon />} />
                        </CardContent>
                    </Card>
                </Grid>
            </Box>
        </>
    )
}