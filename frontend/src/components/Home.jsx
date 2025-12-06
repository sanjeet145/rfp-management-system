import InputBox from "../utils/Input";
import SaveIcon from '@mui/icons-material/Save';
import Stack from '@mui/material/Stack';
import { Activity, useState } from "react";
import IconButton from "../utils/IconButton";
import { login,saveRFP } from "../utils/api";
import { useNavigate } from "react-router-dom";

export default function Home() {
    const [requirement, setRequirement] = useState("")
    const [showLogginBox, setShowLogginBox] = useState(false)
    const navigate = useNavigate()
    const showVendor = () => {
        const userid = localStorage.getItem("userid")
        if (userid === null) {
            setShowLogginBox(true)
            return
        }
        const query={"query":requirement}
        const res = saveRFP(query)
        if(res["status"]===201){
            navigate('/rfps')
            return
        }

    }
    const [email, setEmail] = useState("")
    const handleLogin = async (e) => {
        e.preventDefault()
        const loginData = { "email": email }
        await login(loginData)
        setShowLogginBox(false)
    }
    return (
        <Stack direction="column" spacing={2} height={100}>
            <div style={{ display: "flex", flexDirection: "column", marginTop: "20%", gap: "10px" }}>
                <Activity mode={showLogginBox ? 'hidden' : 'visible'}>
                    <>
                        <InputBox label="Type your requirements" placeholder={"Type your requirements.........."} func={(e) => setRequirement(e.target.value)} />
                        <IconButton name={"Save RFp"} func={showVendor} icon={<SaveIcon />} />
                    </>
                </Activity>
                {showLogginBox && <>
                    <InputBox placeholder={"Enter your registered email here"} label="emai address" func={(e) => setEmail(e.target.value)} />
                    <IconButton func={handleLogin} name={"login"} />
                </>}
            </div>
        </Stack>
    )
}