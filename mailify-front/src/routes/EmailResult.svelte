<script lang="ts">
    import { onMount } from "svelte";

    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";

    import SubjectInput from "../components/email-result/SubjectInput.svelte";
    import ActionButtons from "../components/email-result/ActionButtons.svelte";
    import RecipientInput from "../components/email-result/RecipientInput.svelte";
    import MessageTextArea from "../components/email-result/MessageTextArea.svelte";
    import MailingBackground from "../components/background/MailingBackground.svelte";

    export let recipient = "";
    export let subject = "";
    export let message = "";

    onMount(() => {
        const urlParams = new URLSearchParams(window.location.search);
        recipient = urlParams.get("personEmail") || "";
        subject = urlParams.get("emailSubject") || "";
        message = urlParams.get("email") || "";
    });

    const handleSend = () => {

    };

    const handleSaveDraft = () => {

    };

</script>

<div class="min-h-screen bg-transparent text-midnight font-helvetica">
    <Navbar/>
    <MailingBackground/>

    <div class="flex flex-col gap-10 max-w-screen-lg mx-auto p-8 bg-white/20 shadow-lg backdrop-blur-sm rounded-md border-2 border-stone-300">
        <div class="flex align-middle justify-items-center px-4ww w-full">
            <h3 class="mx-auto text-xl font-bold">Here Are Your Generated Email</h3>
        </div>

        <div class="flex flex-col gap-5 px-4 py-2">
            <RecipientInput bind:value={recipient} />
            <SubjectInput bind:value={subject} />
            <MessageTextArea bind:value={message} />
        </div>

        <div class="flex items-center justify-between px-4 py-2 border-t border-gray-200">
            <ActionButtons onSend={handleSend} onSaveDraft={handleSaveDraft} />
            <span class="text-sm text-gray-500">@Mailify</span>
        </div>
    </div>

    <Footer/>
</div>