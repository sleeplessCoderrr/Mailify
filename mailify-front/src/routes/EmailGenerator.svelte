<script lang="ts">
    import type { Request } from "../lib/interfaces/Request";
    import type {Response} from "../lib/interfaces/Response";
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
    import { navigate } from "svelte-routing";

    let request:Request = {
        purpose: null,
        name: "",
        receiverMail: "",
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

    let progressInterval: ReturnType<typeof setInterval> | null = null;
    let funFactInterval: ReturnType<typeof setInterval> | null = null;

    function setActiveCategory(category: string) { activeCategory = category; }
    function goToResult() { navigate("/page/result"); }

    async function handleSubmit() {
        isLoading = true;
        progress = 0;
        randomFact = getRandomFunFact();

        if (!progressInterval) {
            progressInterval = setInterval(() => {
                if (progress < 95) { 
                    progress += Math.random() * 5; 
                }
            }, 200);
        }

        if (!funFactInterval) {
            funFactInterval = setInterval(() => {
                randomFact = getRandomFunFact();
            }, 5000);
        }

        try {
            request.purpose = activeTab;
            request.goalCategories = activeCategory;

            const generatedEmail = await GenerateEmail(request);
            // ## TODO: Handle response

            console.log("Generated Email:", generatedEmail);
            completeProgress();
            goToResult();
        } catch (error) {
            clearIntervals();
        }
    }

    function completeProgress() {
        progress = 100; 
        setTimeout(() => {
            clearIntervals(); 
        }, 500); 
    }

    function clearIntervals() {
        if (progressInterval) {
            clearInterval(progressInterval);
            progressInterval = null;
        }
        if (funFactInterval) {
            clearInterval(funFactInterval);
            funFactInterval = null;
        }
        isLoading = false;
        progress = 0;
    }
</script>

<div class="min-h-screen bg-transparent text-midnight font-helvetica">
    <LoadingSpinner isLoading={isLoading} progress={progress} funFact={randomFact.funFact} detail={randomFact.detail}/>
    <MailingBackground />
    <Navbar />

    <div class="max-w-screen-md mx-auto p-8 bg-white/20 shadow-lg backdrop-blur-sm rounded-md border-2 border-stone-300">
        <TabSelector activeTab={activeTab} setActiveTab={(tab) => (activeTab = tab)} />
        <InputForm activeTab={activeTab} request={request} />
        <CategorySelector
            categories={categories}
            activeCategory={activeCategory}
            setActiveCategory={setActiveCategory}/>
        <CategoryDescription activeCategory={activeCategory} />
        <button
            class="mt-6 w-full bg-blaze/80 text-white py-2 rounded hover:bg-blaze ease-in-out duration-300"
            on:click={handleSubmit()}>
            Generate Email
        </button>
    </div>
</div>
