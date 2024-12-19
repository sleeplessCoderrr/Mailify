import type { Request } from "../interfaces/Request";

export function EmailPromptBuilder(request: Request, activeTab: "send" | "reply"): { userPrompt: string; start: string } {
    const userPrompt = `Generate an email for ${request.name} to ${request.receiver}. Purpose: ${request.emailGoals}`;
    const start = activeTab === "send" ? "Dear" : "Hi";

    return { userPrompt, start };
}
