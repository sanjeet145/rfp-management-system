import { jwtDecode } from "jwt-decode"

export async function login(loginData) {
    try {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/login`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginData)
        })
        if (response.ok) {
            const res = await response.json()
            const token = res["message"]
            const decoded = jwtDecode(token);
            localStorage.setItem("userid", decoded.sub)
            localStorage.setItem("token", token)
            return { "status": 200, "message": "logged in" }
        }
        return { "status": 401, "message": "Invalid login credentials" }
    } catch (error) {
        return { "status": 401, "message": "Something went wrong" }

    }
}

export async function getvendor(page, perpage, category) {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/get-vendors?category=${category}&page=${page}&perpage=${perpage}`)
    const result = await res.json()
    if (res.ok) {
        return { "status": 200, "message": result.message }
    }
}
export async function getProposalResponses(page, perpage, rfp_id) {
    try {
        const res = await fetch(`${process.env.REACT_APP_API_URL}/proposal-response?page=${page}&perpage=${perpage}`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem("token")}`,
                'Rfpid': rfp_id
            }
        })
        const result = await res.json()
        if (res.ok) {
            return { "status": 200, "message": result.message }
        }
        return { "status": 500, "message": "something went wrong" }
    } catch (error) {
        return { "status": 500, "message": "Something went wrong" }
    }
}

export async function getBestProposal(rfp_id) {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/best-proposal`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`,
            'Rfpid': rfp_id
        }
    })
    const result = await res.json()
    if (res.ok) {
        return { "status": 200, "message": result.message }
    }
}

export async function getrfp(rfp_id) {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/get-rfp`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`,
            'Rfpid': rfp_id
        }
    })
    const result = await res.json()
    if (res.ok) {
        return { "status": 200, "message": result.message }
    }
}



export async function getrfps() {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/get-rfps`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        }
    })
    if (res.ok) {
        const result = await res.json()
        return { "status": 200, "message": result.message }
    } else
        return { "status": 500, "message": "Something went wrong" }

}



export async function saveRFP(query) {
    // save
    // save-rfp {query in data and token in authentication} returns category
    try {
        const res = await fetch(`${process.env.REACT_APP_API_URL}/save-rfp`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem("token")}`
            },
            body: JSON.stringify(query)
        })
        if (res.status === 201) {
            return { "status": 201, "message": "RFP saved successfully" }
        }
        return { "status": 500, "message": "Something went wrong" }
    } catch (error) {
        return { "status": 500, "message": "Something went wrong" }
    }
}

export async function sendProposal(vendorid, rfpid) {
    const data = {
        "rfpid": rfpid,
        "vendorid": vendorid
    }
    const res = await fetch(`${process.env.REACT_APP_API_URL}/send-proposal`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        },
        body: JSON.stringify(data)
    })
    const result = await res.json()
    if (res.ok) {
        alert("Message sent")
        return { "status": 200, "message": result.message }
    }
    return { "status": 500, "message": result.message }

}