export interface Request {
    purpose?: "send" | "reply" | null,
    name:string,
    receiver:string,
    receiverMail:string,
    goalCategories:string,
    emailAbout:string,
}


