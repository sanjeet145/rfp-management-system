import Stack from "@mui/material/Stack";
import IconButton from "../utils/IconButton";
import { useNavigate } from "react-router-dom";
import { Login, VerifiedUser, RequestPage, Home } from "@mui/icons-material"


export default function Navbar() {
    const navigate = useNavigate()
    const func = () => {
        alert("clicked")
    }
    const path = window.location.pathname
    return (
        <Stack direction={"row"} spacing={1} alignItems="center" justifyContent={"space-between"} style={{ boxShadow: "0px -1px 10px  black", marginBottom: "5px", padding: "2px", height: "3rem" }}>
            <h1 style={{ fontSize: "100%" }}>RFP Management System</h1>
            <Stack direction={"row"} spacing={2}>
                {/* <IconButton name={"Login"} func={func}/> */}
                <IconButton name={"Home"} func={() => navigate('/')} icon={<Home />} />
                <IconButton name={"RFP"} func={() => navigate('/rfps')} icon={<RequestPage />} />
                {path === '/' &&
                    <>
                        <IconButton name={"login"} func={() => navigate('/login')} icon={<VerifiedUser />} />
                        <IconButton name={"Register"} func={() => navigate('/register')} icon={<Login />} />
                    </>
                }
            </Stack>
        </Stack>
    )
}