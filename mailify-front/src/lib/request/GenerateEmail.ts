export async function GenerateEmail(userPrompt: string, start: string): Promise<string> {
    try {
        const payload = {
            user_prompt: userPrompt,
            start: start,
        };

        const response = await fetch("http://localhost:5000/generate-email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            throw new Error("Failed to generate email");
        }

        const data = await response.json();
        return data.email || "No email generated. Please try again.";
    } catch (error) {
        console.error("Error:");
        throw error;
    }
}
