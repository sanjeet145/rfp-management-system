import { Box, Card, CardContent, Typography, Grid, Stack } from "@mui/material"
import { getrfps } from "../utils/api"
import { useEffect, useState } from "react"
import IconButton from "../utils/IconButton"
import { useNavigate } from "react-router-dom"

export default function RFPS() {
    const [rfps, setRfps] = useState(null)
    const navigate = useNavigate()
    useEffect(() => {
        const getData = async () => {
            const data = await getrfps()
            if (data["status"] == 200) {
                setRfps(data["message"])
            } else {
                alert(data["message"])
            }
        }
        getData()
    }, [])
    const saveToLocal=(rfpid,category)=>{
        localStorage.setItem("rfpid",rfpid)
        localStorage.setItem("category",category)
    }
    return (
        <>
            <Box>
                <Box sx={{ flexGrow: 1, padding: 2 }}>
                    <Grid container spacing={2}>
                        {rfps && rfps.map((rfp) => (
                            <Grid item xs={12} sm={6} md={4} lg={3} key={rfp.id}>
                                <Card sx={{ height: "100%", padding: 2, display: "flex", flexDirection: "column", justifyContent: "space-between" }}>
                                    <CardContent>
                                        <Typography variant="h6" gutterBottom>
                                            {rfp.item_category}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            <strong>Total Budget:</strong> {rfp.total_budget}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            <strong>Payment Terms:</strong> {rfp.payment_terms}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            <strong>Status:</strong> {rfp.status}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            <strong>Delivery Days:</strong> {rfp.delivery_days}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" sx={{ marginTop: 1 }}>
                                            {rfp.description_raw.length > 60
                                                ? rfp.description_raw.slice(0, 60) + "..."
                                                : rfp.description_raw}
                                        </Typography>
                                    </CardContent>
                                    <Stack direction={"row"} gap={2} justifyContent={"space-between"}>
                                        <IconButton name={"show vendors"} func={()=>{saveToLocal(rfp.id,rfp.item_category); navigate("/vendors")}}/>
                                        <IconButton name={"show responses"} func={()=>{saveToLocal(rfp.id,rfp.item_category); navigate("/responses")}} />
                                    </Stack>
                                </Card>
                            </Grid>
                        ))}
                    </Grid>
                </Box>
            </Box>
        </>
    )
}