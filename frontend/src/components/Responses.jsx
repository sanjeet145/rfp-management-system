import { Box, Card, CardContent, Typography, Grid, Stack } from "@mui/material"
import {  getProposalResponses } from "../utils/api"
import { useEffect, useState } from "react"
import IconButton from "../utils/IconButton"
import { SkipNext, SkipPrevious } from "@mui/icons-material"
import OriginalRfp from "./OriginalRfp"
import BestResponse from "./BestResponse"

export default function Responses() {
    const [proposals, setProposals] = useState(null)
    const [currPage, setCurrPage] = useState(1)
    const [totalPage, setTotalPage] = useState(10)
    const limit = 10
    useEffect(() => {
        const getData = async () => {
            const result = await getProposalResponses(currPage, limit, localStorage.getItem("rfpid"))
            setProposals(result['message'])
        }
        getData()
    }, [currPage])
    return (
        <>
            <Box>
                <OriginalRfp />
                <BestResponse />
                <Grid container spacing={2} gap={5}>
                    {proposals && proposals.map((proposal) => (
                        <Grid item xs={12} sm={6} md={4} lg={3} key={proposal.id}>
                            <Card sx={{ height: "100%", padding: 2, display: "flex", flexDirection: "column", justifyContent: "space-between", boxShadow: "0px 1px 1px black" }}>
                                <CardContent>
                                    <Typography variant="h6" gutterBottom>
                                        {proposal.vendor.company_name}
                                    </Typography>
                                    <Typography variant="body2" color="textSecondary">
                                        <strong>Email:</strong> {proposal.vendor.email}
                                    </Typography>
                                    <Typography variant="body2" color="textSecondary">
                                        <strong>Phone:</strong> {proposal.vendor.phone}
                                    </Typography>
                                    <Typography variant="body2" color="textSecondary">
                                        <strong>Responses:</strong>
                                    </Typography>
                                    <Stack spacing={2} mt={1}>
                                        {proposal.response.map((response, index) => (
                                            <>
                                                <Box key={response.id} sx={{ paddingLeft: 1 }}>
                                                    <Typography variant="body2" color="textSecondary">
                                                        <strong>{index + 1}.</strong>
                                                    </Typography>
                                                    <Typography variant="body2" color="textSecondary">
                                                        <strong>vendor delivery days: </strong> {response.vendor_delivery_days}
                                                    </Typography>
                                                    <Typography variant="body2" color="textSecondary">
                                                        <strong>Total price: </strong> {response.vendor_total_price}
                                                    </Typography>
                                                    <Typography variant="body2" color="textSecondary">
                                                        <strong>vendor warranty years: </strong> {response.vendor_warranty_years}
                                                    </Typography>
                                                    <Typography variant="body2" color="textSecondary">
                                                        <strong>Notes </strong> {response.notes}
                                                    </Typography>
                                                    <Stack spacing={2} mt={1}>
                                                        {response.items.map((item, idx) => (
                                                            <Box key={item.id} sx={{ paddingLeft: 1 }}>
                                                                <Typography variant="body2" color="textSecondary">
                                                                    <strong>{idx + 1}.</strong> {item.item_name}
                                                                </Typography>
                                                                <Typography variant="body2" color="textSecondary" sx={{ ml: 2 }}>
                                                                    <strong>Unit Price:</strong> {item.unit_price}
                                                                </Typography>
                                                                <Typography variant="body2" color="textSecondary" sx={{ ml: 2 }}>
                                                                    <strong>Total Price:</strong> {item.total_price}
                                                                </Typography>
                                                            </Box>
                                                        ))}
                                                    </Stack>
                                                </Box>
                                            </>
                                        ))}
                                    </Stack>
                                    {/* <Typography variant="body2" color="textSecondary" sx={{ marginTop: 1 }}>
                                            <strong>Address: </strong>{vendor.address.length > 60
                                                ? vendor.address.slice(0, 60) + "..."
                                                : vendor.address}
                                        </Typography> */}
                                </CardContent>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
                <div style={{ marginTop: "50px" }}>
                    <IconButton name={"previous page"} icon={<SkipPrevious />} func={() => { setCurrPage((currPage + 1) % totalPage) }} />
                    <IconButton name={"next page"} icon={<SkipNext />} func={() => { setCurrPage((currPage - 1) % totalPage) }} />
                </div>
            </Box>
        </>
    )
}