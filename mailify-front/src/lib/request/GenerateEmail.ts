import axios from 'axios';
import type { Request } from "../interfaces/Request";
import type { Response } from "../interfaces/Response";

export async function GenerateEmail(request: Request): Promise<Response> {
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
            const response: Response = {
                'personEmail': data.person_mail,
                'email': data.generated_email,
                'emailSubject': data.email_subject,
            };

            console.log(response);
            return response;
        } else {
            console.error("No data received in response.");
            throw new Error("Failed to generate email");
        }
        
    } catch (error) {
        console.error("Error:", error); 
        throw error;
    }
}
