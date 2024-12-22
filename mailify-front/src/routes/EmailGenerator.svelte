<script lang="ts">
    import type { Request } from "../lib/interfaces/Request";
    import type { FunFact } from "../lib/interfaces/FunFact";

    import { getRandomFunFact } from "../lib/interfaces/FunFact";
    import { GenerateEmail } from "../lib/request/GenerateEmail";

    import Navbar from "../components/Navbar.svelte";
    import LoadingSpinner from "../components/ui/LoadingSpinner.svelte";
    import InputForm from "../components/email-generator/InputForm.svelte";
    import TabSelector from "../components/email-generator/TabSelector.svelte";
    import MailingBackground from "../components/background/MailingBackground.svelte";
    import CategorySelector from "../components/email-generator/CategorySelector.svelte";
    import CategoryDescription from "../components/email-generator/CategoryDescription.svelte";

    let request:Request = {
        purpose: null,
        name: "",
        receiver: "",
        goalCategories: "",
        emailAbout: "",
    };

    // For Email Generator
    const categories = ["Applying Job", "College"];
    let activeCategory: string = "Applying Job";
    let activeTab: "send" | "reply" = "send";

    //For Loading Spinner
    let isLoading: boolean = false;
    let progress: number = 0;
    let randomFact: FunFact = getRandomFunFact();

    function setActiveCategory(category: string) {
        activeCategory = category;
    }

    async function handleSubmit() {
        isLoading = true;
        request.purpose = activeTab;
        request.goalCategories = activeCategory;
        
        try {
            const generatedEmail = await GenerateEmail(request);
            // ## To Do: Display the generated email in a modal or a new page.

        } catch (error) {
            console.log("Something went wrong while generating the email.");
        }
    }

    let interval = setInterval(() => {
        if (progress < 100) {
            progress += Math.floor(Math.random() * (10 - 1 + 1)) + 1;
            if (progress % 20 === 0) {
                randomFact = getRandomFunFact(); 
            }
        } else {
            clearInterval(interval);
            isLoading = false; 
            progress = 0;
        }
    }, 500)
</script>

<div class="min-h-screen bg-transparent text-midnight font-helvetica">
    <LoadingSpinner isLoading={isLoading} progress={progress} funFact={randomFact.funFact} detail={randomFact.detail}/>
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
