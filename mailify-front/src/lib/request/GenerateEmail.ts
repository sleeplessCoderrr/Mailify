import axios from 'axios';
import type { Request } from "../interfaces/Request";

export async function GenerateEmail(request: Request): Promise<string> {
    try {
        const response = await axios.post("http://localhost:5000/generate-email", request, {
            headers: {
                "Content-Type": "application/json",
            }
        });

        const data = response.data;

        if (data != null) {
            return data.email;
        } else {
            throw new Error("Failed to generate email");
        }
        
    } catch (error) {
        console.error("Error:", error);
        throw error;
    }
}
