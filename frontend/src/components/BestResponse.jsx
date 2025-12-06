import { useEffect, useState } from "react"
import { getBestProposal } from "../utils/api"
import { Box, Card, CardContent, Typography, Grid, Stack } from "@mui/material"


export default function BestResponse() {
    const [proposal, setProposal] = useState(null)
    const [vendor, setVendor] = useState(null)
        useEffect(() => {
            const getData = async () => {
                const res = await getBestProposal(localStorage.getItem('rfpid'))
                setProposal(res["message"]["proposal"])
                setVendor(res["message"]["vendor"])
            }
            getData()
        }, [])
    return (
        <>
            { proposal && vendor &&
                <Box sx={{ flexGrow: 1, padding: 2 }}>
                    <Grid item xs={12} sm={6} md={4} lg={3}>
                        <Card sx={{ height: "100%", padding: 2, display: "flex", flexDirection: "column", justifyContent: "space-between", boxShadow: "0px 1px 1px black" }}>
                            <CardContent>
                                <Typography variant="h6" gutterBottom>
                                    Best Proposal
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Company name :</strong> {vendor.company_name}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Vendor :</strong> {vendor.name}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Phone :</strong> {vendor.phone}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Email :</strong> {vendor.email}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Summary :</strong> {proposal.summary_ai}
                                </Typography>
                                {/* <Typography variant="body2" color="textSecondary">
                                    <strong>Response:</strong>
                                </Typography> */}
                            </CardContent>
                        </Card>
                    </Grid>
                </Box>
            }
        </>
    )
}