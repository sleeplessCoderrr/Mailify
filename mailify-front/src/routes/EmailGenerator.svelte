<script lang="ts">
    import type { Request } from "../lib/interfaces/Request";
    import { GenerateEmail } from "../lib/request/GenerateEmail";
    import { EmailPromptBuilder } from "../lib/request/EmailPromptBuilder";

    import Navbar from "../components/Navbar.svelte";
    import InputForm from "../components/email-generator/InputForm.svelte";
    import TabSelector from "../components/email-generator/TabSelector.svelte";
    import MailingBackground from "../components/background/MailingBackground.svelte";
    import CategorySelector from "../components/email-generator/CategorySelector.svelte";
    import CategoryDescription from "../components/email-generator/CategoryDescription.svelte";

    let request:Request = {
        name: "",
        receiver: "",
        emailGoals: "",
        activeCategory: "",
    };

    const categories = ["Applying Job", "College"];
    let activeCategory: string = "Applying Job";
    let activeTab: "send" | "reply" = "send";

    function setActiveCategory(category: string) {
        activeCategory = category;
    }

    async function handleSubmit() {
        try {
            const { userPrompt, start } = EmailPromptBuilder(request, activeTab);
            const generatedEmail = await GenerateEmail(userPrompt, start);

            alert("Email content generated successfully!");
        } catch (error) {
            alert("Something went wrong while generating the email.");
        }
    }
</script>

<div class="min-h-screen bg-transparent text-midnight font-helvetica">
    <MailingBackground />
    <Navbar />

    <div class="max-w-screen-md mx-auto mt-10 p-8 bg-white/20 shadow-lg backdrop-blur-sm rounded-md border-2 border-stone-300">
        <TabSelector activeTab={activeTab} setActiveTab={(tab) => (activeTab = tab)} />
        <InputForm activeTab={activeTab} request={request} />
        <CategorySelector
            categories={categories}
            activeCategory={activeCategory}
            setActiveCategory={setActiveCategory}/>
        <CategoryDescription activeCategory={activeCategory} />
        <button
            class="mt-6 w-full bg-blaze/80 text-white py-2 rounded hover:bg-blaze ease-in-out duration-300"
            on:click={handleSubmit}>
            Generate Email
        </button>
    </div>
</div>
