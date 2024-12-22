export interface FunFact {
    funFact: string;
    detail: string;
}
  
export const funFacts: FunFact[] = [
    {
      funFact: "Your resume is like your bio!",
      detail: "Keep it short, highlight your best skills, and make it easy to scan."
    },
    {
      funFact: "TikTok skills count!",
      detail: "Social media know-how is a top skill for entry-level jobs."
    },
    {
      funFact: "80% of jobs need no experience.",
      detail: "Focus on your soft skills like teamwork and creativity!"
    },
    {
      funFact: "Cover letters = elevator pitch.",
      detail: "Show why you're the perfect fit in a few personalized sentences."
    },
    {
      funFact: "Beat the ATS bots!",
      detail: "Use job keywords to get your resume noticed by recruiters."
    },
    {
      funFact: "Networking isn’t scary!",
      detail: "Reach out on LinkedIn or talk to alumni to grow connections."
    },
    {
      funFact: "You don’t need to be perfect.",
      detail: "If you meet 60% of the qualifications, apply anyway!"
    },
    {
      funFact: "Gen Z powers = tech-savvy.",
      detail: "Your digital skills and adaptability are in high demand."
    },
    {
      funFact: "Hobbies can be skills.",
      detail: "Gaming, editing, or volunteering showcase real talents!"
    },
    {
      funFact: "Rejection means redirection.",
      detail: "Every 'no' is a step closer to your first 'yes.' Keep going!"
    }
];
  
export const getFunFacts = (): FunFact[] => {
    return funFacts;
};
  
export const getRandomFunFact = (): FunFact => {
    const randomIndex = Math.floor(Math.random() * funFacts.length);
    return funFacts[randomIndex];
};
  