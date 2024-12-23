<script lang="ts">
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";

    import SubjectInput from "../components/email-result/SubjectInput.svelte";
    import ActionButtons from "../components/email-result/ActionButtons.svelte";
    import RecipientInput from "../components/email-result/RecipientInput.svelte";
    import MessageTextArea from "../components/email-result/MessageTextArea.svelte";
    import MailingBackground from "../components/background/MailingBackground.svelte";

    let recipient = '';
    let subject = '';
    let message = '';

    const handleSend = () => {

    };

    const handleSaveDraft = () => {

    };

</script>

<div class="min-h-screen bg-transparent text-midnight font-helvetica">
    <Navbar/>
    <MailingBackground/>

    <div class="max-w-screen-md mx-auto p-8 bg-white/20 shadow-lg backdrop-blur-sm rounded-md border-2 border-stone-300">
        <div class="flex items-center justify-between px-4 py-2 border-b border-gray-200">
            <h3 class="text-xl font-bold">Email Result</h3>
        </div>

        <div class="px-4 py-2">
            <RecipientInput bind:value={recipient} />
            <SubjectInput bind:value={subject} />
            <MessageTextArea bind:value={message} />
        </div>

        <div class="flex items-center justify-between px-4 py-2 border-t border-gray-200">
            <ActionButtons onSend={handleSend} onSaveDraft={handleSaveDraft} />
            <span class="text-sm text-gray-500">95% of storage used.</span>
        </div>
    </div>

    <Footer/>
</div>