import { useEffect, useState } from "react"
import { getrfp } from "../utils/api"
import { Box, Card, CardContent, Typography, Grid, Stack } from "@mui/material"


export default function OriginalRfp() {
    const [rfp, setRfp] = useState(null)
        useEffect(() => {
            const getData = async () => {
                const res = await getrfp(localStorage.getItem('rfpid'))
                setRfp(res["message"])
            }
            getData()
        }, [])
    return (
        <>
            {rfp &&
                <Box sx={{ flexGrow: 1, padding: 2 }}>
                    <Grid item xs={12} sm={6} md={4} lg={3} key={rfp.id}>
                        <Card sx={{ height: "100%", padding: 2, display: "flex", flexDirection: "column", justifyContent: "space-between", boxShadow: "0px 1px 1px black" }}>
                            <CardContent>
                                <Typography variant="h6" gutterBottom>
                                    Your Requirements
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Category :</strong> {rfp.item_category}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Warranty:</strong> {rfp.warranty_min_years}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Payment terms:</strong> {rfp.payment_terms}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Budget:</strong> {rfp.total_budget}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Delivery Days:</strong> {rfp.delivery_days}
                                </Typography>
                                <Typography variant="body2" color="textSecondary">
                                    <strong>Items:</strong>
                                </Typography>
                                <Stack spacing={2} mt={1}>
                                    {rfp.items.map((item, index) => (
                                        <Box key={item.id} sx={{ paddingLeft: 1 }}>
                                            <Typography variant="body2" color="textSecondary">
                                                <strong>{index + 1}.</strong> {item.name}
                                            </Typography>
                                            <Typography variant="body2" color="textSecondary" sx={{ ml: 2 }}>
                                                <strong>Quantity:</strong> {item.quantity}
                                            </Typography>
                                            <Typography variant="body2" color="textSecondary" sx={{ ml: 2 }}>
                                                <strong>Specification:</strong> {item.specifications}
                                            </Typography>
                                        </Box>
                                    ))}
                                </Stack>
                                <Typography variant="body2" color="textSecondary" sx={{ marginTop: 1 }}>
                                    <strong>description: </strong>{rfp.description_raw.length > 60
                                        ? rfp.description_raw.slice(0, 60) + "..."
                                        : rfp.description_raw}
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                </Box>
            }
        </>
    )
}