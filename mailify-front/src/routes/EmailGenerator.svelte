<script lang="ts">
    import type {Request} from "../lib/interfaces/Request";

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

    function handleSubmit() {
        console.log(request);
        alert("Email content generated!");
    }
</script>

<div class="min-h-screen bg-transparent text-midnight font-helvetica">
    <MailingBackground />
    <Navbar />

    <div class="max-w-4xl mx-auto mt-16 p-8 bg-white/20 shadow-lg backdrop-blur-sm rounded-md border-2 border-stone-300">
        <TabSelector activeTab={activeTab} setActiveTab={(tab) => (activeTab = tab)} />
        <InputForm activeTab={activeTab} request={request} />
        <CategorySelector
            categories={categories}
            activeCategory={activeCategory}
            setActiveCategory={setActiveCategory}
        />
        <CategoryDescription activeCategory={activeCategory} />
        <button
                class="mt-6 w-full bg-blaze/80 text-white py-2 rounded hover:bg-blaze ease-in-out duration-300"
                on:click={handleSubmit}
        >
            Generate Email
        </button>
    </div>
</div>
