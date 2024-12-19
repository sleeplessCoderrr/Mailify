import axios from 'axios';
import type { Request } from "../interfaces/Request";

export async function GenerateEmail(request: Request): Promise<string> {
    try {
        console.log("Request sent to Flask API:", request);

        const response = await axios.post("http://localhost:5000/generate-email", request, {
            headers: {
                "Content-Type": "application/json",
            }
        });

        console.log("Response from Flask API:", response); 
        const data = response.data;

        if (data != null) {
            console.log("Generated email:", data.generated_email); 
            return data.generated_email;
        } else {
            console.error("No data received in response.");
            throw new Error("Failed to generate email");
        }
        
    } catch (error) {
        console.error("Error:", error); 
        throw error;
    }
}
