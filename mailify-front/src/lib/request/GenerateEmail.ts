import axios from "axios";
import type { Request } from "../interfaces/Request";
import type { Response } from "../interfaces/Response";

const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000';
export async function GenerateEmail(request: Request): Promise<Response> {
    try {
        console.log("Request sent to Flask API:", request);

        const response = await axios.post(`${BASE_URL}/generate-email`, request, {
            headers: {
                "Content-Type": "application/json",
            },
        });

        const data = response.data;
        if (data 
            && data.person_email 
            && data.generated_email 
            && data.generated_subject) {
            const result: Response = {
                personEmail: data.person_email,
                emailSubject: data.generated_subject,
                email: data.generated_email,
            };
            
            console.log(result);
            return result;
        } else {
            console.error("Invalid response structure:", data);
            throw new Error("Failed to generate email: Invalid response structure");
        }
    } catch (error: any) {
        console.error("Error:", error.message || error);
        throw new Error(error.response?.data?.error || "Failed to generate email");
    }
}

