<script lang="ts">
    import { onMount } from "svelte";
    import { navigate } from "svelte-routing";

    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import SendModal from "../components/modal/SendModal.svelte";
    import SubjectInput from "../components/email-result/SubjectInput.svelte";
    import ActionButtons from "../components/email-result/ActionButtons.svelte";
    import RecipientInput from "../components/email-result/RecipientInput.svelte";
    import MessageTextArea from "../components/email-result/MessageTextArea.svelte";
    import MailingBackground from "../components/background/MailingBackground.svelte";

    let recipient = "";
    let subject = "";
    let message = "";

    onMount(() => {
        const urlParams = new URLSearchParams(window.location.search);
        recipient = urlParams.get("recipient") || "";
        subject = urlParams.get("subject") || "";
        message = urlParams.get("message") || "";
    });

    let isVisible: boolean = false;
    let title: string = "Choose The Platform";

    const handleGmail = () => {
        const mailtoLink = `https://mail.google.com/mail/?view=cm&fs=1&to=${recipient}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(message)}`;
        window.open(mailtoLink, "_blank");
    }

    const handleOutlook = () => {
        const mailtoLink = `https://outlook.office.com/mail/deeplink/compose?to=${recipient}&subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(message)}`;
        window.open(mailtoLink, "_blank");
    }
</script>

<div class="min-h-screen bg-transparent text-midnight font-helvetica">
    <Navbar/>
    <MailingBackground/>
    <SendModal isVisible={isVisible} title={title} onGmail={handleGmail} onOutlook={handleOutlook} />

    <div class="flex flex-col gap-10 max-w-screen-lg mx-auto p-8 bg-white/20 mb-24 mt-6 shadow-lg backdrop-blur-sm rounded-md border-2 border-stone-300">
        <div class="flex align-middle justify-items-center px-4ww w-full">
            <h3 class="mx-auto text-xl font-bold">Here Are Your Generated Email</h3>
        </div>

        <div class="flex flex-col gap-5 px-4 py-2">
            <RecipientInput bind:value={recipient} />
            <SubjectInput bind:value={subject} />
            <MessageTextArea bind:value={message} />
        </div>

        <div class="flex items-center justify-between px-4 py-2 border-t border-gray-200">
            <ActionButtons onSend={()=>(isVisible = true)} onGenerate={()=>(navigate('/page/mailing'))} />
            <span class="text-sm text-gray-500">@Mailify</span>
        </div>
    </div>
    <Footer/>
</div>