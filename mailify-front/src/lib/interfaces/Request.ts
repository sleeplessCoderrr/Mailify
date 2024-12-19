export interface Request {
    purpose?: "send" | "reply" | null,
    name:string,
    receiver:string,
    goalCategories:string,
    emailAbout:string,
}


