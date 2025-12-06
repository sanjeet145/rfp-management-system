import { Box, Card, CardContent, Typography, Grid, Stack, listItemTextClasses } from "@mui/material"
import { getvendor, sendProposal } from "../utils/api"
import { useEffect, useState } from "react"
import IconButton from "../utils/IconButton"
import { useNavigate } from "react-router-dom"
import {Send, SkipNext,SkipPrevious} from "@mui/icons-material"

export default function Vendors() {
    const [vendors, setVendors] = useState(null)
    const category = localStorage.getItem("category")
    const [currPage, setCurrPage] = useState(1)
    const [totalPage, setTotalPage] = useState(1)
    const limit =10
    useEffect(() => {
        const getData = async () => {
            if(category===undefined || currPage===undefined ||limit===undefined)
                return
            const data = await getvendor(currPage,limit,category)
            if (data["status"] === 200) {
                setVendors(data["message"]["items"])
                setTotalPage(data["message"]["total"])
            } else {
                alert(data["message"])
            }
        }
        getData()
    }, [currPage])
    return (
        <>
            <Box>
                <Box sx={{ flexGrow: 1, padding: 2 }}>
                    <Grid container spacing={2} gap={5}>
                        {vendors && vendors.map((vendor) => (
                            <Grid item xs={12} sm={6} md={4} lg={3} key={vendor.id}>
                                <Card sx={{ height: "100%", padding: 2, display: "flex", flexDirection: "column", justifyContent: "space-between" , boxShadow:"0px 1px 1px black"}}>
                                    <CardContent>
                                        <Typography variant="h6" gutterBottom>
                                            {vendor.company_name}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            <strong>Owner Name:</strong> {vendor.name}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            <strong>Phone:</strong> {vendor.phone}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            <strong>Email:</strong> {vendor.email}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" sx={{ marginTop: 1 }}>
                                            <strong>Address: </strong>{vendor.address.length > 60
                                                ? vendor.address.slice(0, 60) + "..."
                                                : vendor.address}
                                        </Typography>
                                    </CardContent>
                                    <Stack direction={"row"} gap={2} justifyContent={"space-between"}>
                                        <IconButton name={"send proposal"} icon={<Send/>} func={()=>{sendProposal(vendor.id,localStorage.getItem("rfpid"))}}/>
                                    </Stack>
                                </Card>
                            </Grid>
                        ))}
                    </Grid>
                </Box>
                <div style={{marginTop:"50px"}}>
                    <IconButton name={"previous page"} icon={<SkipPrevious/>} func={()=>{setCurrPage((currPage+1)%totalPage)}}/>
                    <IconButton name={"next page"} icon={<SkipNext/>} func={()=>{setCurrPage((currPage-1)%totalPage)}}/>
                </div>
            </Box>
        </>
    )
}